# app_interativo_export_html_kinfo_nomeavel_numindex_ordem.py

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re
from scipy.signal import find_peaks, peak_widths
import itertools
import pandas as pd

# Tela inicial
st.set_page_config(page_title="XRD Interativo — Exportar HTML", layout="wide")
st.title("Análise XRD — Exportação HTML")

# Controle de K
K_input = st.number_input(
    "Fator de forma K para equação de Scherrer",
    min_value=0.1, max_value=2.0, value=0.9, step=0.01,
    format="%.2f",
    help="Altere K (geralmente entre 0.7-1.0). Padrão = 0.9"
)

# ==== Funções auxiliares ====


def load_profile_ascii(file):
    """Lê arquivos .txt com colunas numéricas."""
    xs, ys = [], []
    for ln in file.read().decode('utf-8', errors='ignore').splitlines():
        m = re.findall(
            r'([-+]?\d+(?:\.\d+)?)\s+([-+]?\d+(?:\.\d+)?)$', ln.strip())
        if m:
            a, b = m[0]
            xs.append(float(a))
            ys.append(float(b))
    return np.array(xs), np.array(ys)


def load_csv(file):
    """Lê arquivos .csv de duas colunas."""
    data = np.loadtxt(file, delimiter=',')
    return data[:, 0], data[:, 1]


def scherrer_size(beta_rad, theta_rad, wavelength=1.5406, K=0.9):
    """Equação de Scherrer: D = (K * λ) / (β * cosθ)."""
    eps = 1e-12
    beta_rad = np.clip(beta_rad, eps, None)
    denom = np.clip(beta_rad * np.cos(theta_rad), eps, None)
    return (K * wavelength) / denom


def analisar_difratograma(two_theta, intensity, K_factor=0.9,
                          min_dist_deg=0.5, prominence_frac=0.10, height_frac=0.05):
    """Identifica picos e calcula Scherrer para os até 10 mais intensos, e retorna ordenados por 2θ."""
    delta = np.mean(np.diff(two_theta))
    distance = max(1, int(min_dist_deg / delta))
    max_int = np.max(intensity)
    prom, height = max_int * prominence_frac, max_int * height_frac

    peaks, _ = find_peaks(intensity, distance=distance,
                          prominence=prom, height=height)
    widths, _, _, _ = peak_widths(intensity, peaks, rel_height=0.5)
    fwhm_deg = widths * delta

    intens_peaks = intensity[peaks]
    N_PEAKS = 10
    N = min(N_PEAKS, len(intens_peaks))
    idx_top = np.argsort(intens_peaks)[-N:][::-1]

    results, annots = [], []
    for j in idx_top:
        pk = peaks[j]
        th2 = two_theta[pk]
        fw = fwhm_deg[j]
        theta, beta = np.deg2rad(th2 / 2), np.deg2rad(fw)
        D = scherrer_size(beta, theta, K_factor)
        results.append({
            "2θ (°)": th2,
            "FWHM (°)": fw,
            "D (Å)": D,
            "Intensidade": intensity[pk]
        })
        annots.append((th2, intensity[pk], f"{th2:.2f}°"))

    # Ordenar resultados pela posição de 2θ crescente
    results = sorted(results, key=lambda r: r["2θ (°)"])
    return results, annots

# ==== Interface principal ====


uploaded_files = st.file_uploader(
    "Envie quantos arquivos quiser (.txt e .csv)",
    type=['txt', 'csv'],
    accept_multiple_files=True
)

if uploaded_files:
    color_cycle = itertools.cycle([
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
    ])

    traces, legenda, resultados = [], [], {}

    for file in uploaded_files:
        name, ext = file.name, file.name.split('.')[-1].lower()
        cor = next(color_cycle)
        legenda.append((name, cor))

        if ext == 'txt':
            two, intensity = load_profile_ascii(file)
        elif ext == 'csv':
            two, intensity = load_csv(file)
        else:
            st.warning(f"Extensão não reconhecida: {name}")
            continue

        results, annots = analisar_difratograma(
            two, intensity, K_factor=K_input)
        resultados[name] = results

        traces.append(go.Scatter(x=two, y=intensity, mode='lines',
                                 name=name, line=dict(color=cor)))
        for th2, ypk, label in annots:
            traces.append(go.Scatter(x=[th2], y=[ypk], mode='markers',
                                     name=f"{name} pico {label}",
                                     marker=dict(color=cor, symbol='x')))

    st.subheader("Arquivos carregados e cores atribuídas")
    for name, cor in legenda:
        st.markdown(
            f"- <span style='color:{cor}'>{name}</span>", unsafe_allow_html=True)

    st.subheader("Resultados por arquivo")
    for name, res in resultados.items():
        st.write(f"**{name}**")
        df = pd.DataFrame(res)
        df.index = df.index + 1
        st.table(df)

    fig = go.Figure(traces)
    fig.update_layout(
        title="Difratograma — Todas Amostras e Referências",
        xaxis_title="2θ (°)", yaxis_title="Intensidade (u.a.)",
        hovermode="x unified"
    )
    st.subheader("Gráfico Interativo")
    st.plotly_chart(fig, use_container_width=True)

    nome_relatorio = st.text_input(
        "Nome do arquivo de relatório (sem extensão)", value="relatorio_xrd"
    )

    html_tables = "".join(
        f"<h2>{name}</h2>\n{pd.DataFrame(res).to_html(index=True)}<br>\n"
        for name, res in resultados.items()
    )

    html_report = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Relatório XRD</title></head><body>
  <h1>Relatório de Análise XRD</h1>
  <h3>Fator de forma K utilizado: {K_input}</h3>
  <h2>Arquivos carregados</h2>
  <ul>{''.join(f'<li>{name}</li>' for name in resultados.keys())}</ul>
  <h2>Resultados por arquivo</h2>
  {html_tables}
  <h2>Gráfico Interativo</h2>
  {fig.to_html(full_html=False, include_plotlyjs="cdn")}
</body></html>"""

    html_bytes = html_report.encode("utf-8")

    st.download_button(
        "📥 Baixar relatório (HTML interativo)",
        data=html_bytes,
        file_name=f"{nome_relatorio}.html",
        mime="text/html"
    )
