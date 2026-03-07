# XRD Analysis Tool — Automação de Difratogramas e Equação de Scherrer

Este projeto foi desenvolvido como parte do **Trabalho de Conclusão de Curso (TCC)** de **Geremias Garcia Berto**, no curso de **Tecnologia em Análise e Desenvolvimento de Sistemas** do **Instituto Federal do Paraná (IFPR) — Campus Paranaguá**.

O software tem como objetivo **automatizar a análise de difratogramas de raios X (DRX)**, permitindo a identificação automática de picos, a estimativa do tamanho médio de cristalitos por meio da **Equação de Scherrer**, e a geração de **relatórios interativos em HTML**.

---

# 🔬 Sobre o Projeto

A **Difração de Raios X (DRX)** é uma técnica amplamente utilizada na **Engenharia de Materiais** para investigar a estrutura cristalina de substâncias.

Na prática experimental, os difratômetros produzem **difratogramas** — gráficos de intensidade da radiação difratada em função do ângulo **2θ**. A análise manual desses dados pode ser **lenta, repetitiva e sujeita a erros**, especialmente quando realizada em planilhas ou softwares genéricos.

Este projeto propõe uma solução computacional para **automatizar etapas importantes dessa análise**, incluindo:

* leitura de dados experimentais
* detecção automática de picos
* cálculo do tamanho médio de cristalitos
* visualização gráfica interativa
* geração de relatórios científicos

---

# 🌐 Aplicação Online

A aplicação pode ser acessada diretamente no navegador:

**https://xrd-analysis-tool.streamlit.app/**

Não é necessário instalar nada para utilizar a ferramenta.

---

# ⚙️ Principais Funcionalidades

### 📂 Processamento automático de arquivos

* Importação de arquivos `.txt` e `.csv`
* Suporte a **múltiplos difratogramas simultaneamente**
* Leitura automática de dados numéricos

### 📈 Detecção automática de picos

* Identificação dos picos de difração mais intensos
* Cálculo automático da **largura à meia altura (FWHM)**

### 🧪 Estimativa do tamanho de cristalitos

Aplicação da **Equação de Scherrer**:

[
D = \frac{K \cdot \lambda}{\beta \cdot \cos\theta}
]

Onde:

* **D** → tamanho médio do cristalito
* **K** → fator de forma (ajustável pelo usuário)
* **λ** → comprimento de onda da radiação (padrão **1.5406 Å — Cu Kα**)
* **β** → largura do pico à meia altura (**FWHM**) em radianos
* **θ** → ângulo de Bragg

A equação fornece **uma estimativa do tamanho médio de cristalitos**, sendo amplamente utilizada na caracterização de materiais nanocristalinos.

### 📊 Visualização interativa

* Gráficos interativos com **Plotly**
* Zoom e inspeção de dados
* Comparação visual de múltiplos difratogramas

### 📑 Exportação de relatório

* Geração automática de **relatórios HTML interativos**
* Tabelas com resultados calculados
* Gráficos incorporados ao relatório

---

# 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido em **Python**, utilizando as seguintes bibliotecas:

| Biblioteca    | Finalidade                          |
| ------------- | ----------------------------------- |
| **Streamlit** | Interface web interativa            |
| **NumPy**     | Processamento numérico              |
| **SciPy**     | Detecção de picos e cálculo de FWHM |
| **Plotly**    | Gráficos interativos                |
| **Pandas**    | Estruturação de dados e tabelas     |

---

# 🚀 Como Executar o Projeto Localmente

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/xrd-analysis-tool.git
cd xrd-analysis-tool
```

---

## 2️⃣ Criar ambiente virtual (recomendado)

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Executar a aplicação

```bash
streamlit run xrd-analysis-tool.py
```

Após executar o comando, a interface abrirá automaticamente no navegador (geralmente em):

```
http://localhost:8501
```

---

# 📂 Estrutura do Projeto

```
xrd-analysis-tool/
│
├── xrd-analysis-tool.py     # Código principal da aplicação
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação
```

---

# 📄 Formato de Entrada dos Dados

Os arquivos devem conter **duas colunas numéricas**:

```
2θ   intensidade
```

Exemplo de arquivo `.txt`:

```
20.01 120
20.05 135
20.10 210
20.15 350
20.20 180
```

---

# 🎓 Contexto Acadêmico

Este software foi desenvolvido no contexto do **Trabalho de Conclusão de Curso** intitulado:

**"Difração de Raios X e a Equação de Scherrer na Análise de Materiais"**

Instituição:

**Instituto Federal do Paraná (IFPR) — Campus Paranaguá**

Orientação:

* Prof. **Bruno de Sá Beckerle**
* Profa. **Maria Carolina de Oliveira**

O projeto tem como objetivo **apoiar atividades de ensino e pesquisa na área de caracterização de materiais**.

---

# 📚 Referências Científicas

SCHERRER, P.
*Bestimmung der Größe und der inneren Struktur von Kolloidteilchen mittels Röntgenstrahlen*.
Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, 1918.

CULLITY, B. D.; STOCK, S. R.
*Elements of X-Ray Diffraction*. Prentice Hall.

KLUG, H. P.; ALEXANDER, L. E.
*X-Ray Diffraction Procedures*. Wiley.

---

# 👨‍💻 Autor

**Geremias Garcia Berto**

Tecnologia em Análise e Desenvolvimento de Sistemas
Instituto Federal do Paraná — Campus Paranaguá

GitHub:
https://github.com/Geremias-Garcia

---

# 📄 Licença

Este projeto é disponibilizado **para fins acadêmicos e educacionais**.
