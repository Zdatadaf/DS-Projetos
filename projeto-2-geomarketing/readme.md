# Inteligência de Varejo: Geomarketing Dashboard


## Sobre o Projeto
Este é um projeto de **Inteligência Geográfica (Geomarketing)** focado na análise de expansão de varejo para a Região Metropolitana de Belém (RMB).

O dashboard cruza dados demográficos (densidade populacional e renda) com a localização atual de unidades operacionais para identificar **"Vazios de Mercado"** — áreas com alto potencial de consumo que ainda não são atendidas pela rede.

O sistema utiliza geração de dados sintéticos baseada em **clusters urbanos reais** (Belém Centro, Augusto Montenegro, Icoaraci, Ananindeua Centro e Cidade Nova), garantindo verossimilhança geográfica.

## Funcionalidades
* **Mapeamento de Demanda:** Visualização de clusters de população e renda média através de mapas de calor (Heatmaps).
* **Análise de Cobertura:** Plotagem das lojas existentes para identificar canibalização ou áreas descobertas.
* **Geração de Dados Localizada:** Algoritmo customizado que gera dados demográficos respeitando a geografia real de Belém e Ananindeua (evitando pontos em áreas de rios/floresta).
* **Filtros Dinâmicos:** Segmentação por zonas da cidade e faixas de renda para refinar a busca por novos pontos.

## Lógica e Aplicabilidade (Transfer Learning)
A arquitetura de análise espacial desenvolvida neste projeto é agnóstica e pode ser transferida para **Planejamento Urbano e Setor Público**:

1.  **Varejo:** Site Selection (onde abrir nova loja).
2.  **Saúde:** Mapeamento de epidemias ou localização de novas UBS baseada na densidade de idosos.
3.  **Educação (Zoneamento Escolar):** Otimização de rotas de transporte escolar e identificação de demanda reprimida por creches (substituindo "Renda" por "Vulnerabilidade Social" e "Lojas" por "Escolas").

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Frontend:** Streamlit
* **Visualização Geoespacial:** Plotly Express (Mapbox)
* **Manipulação de Dados:** Pandas / NumPy

## Como Rodar o Projeto

1. Clone este repositório:
```bash
git clone [https://github.com/SEU-USUARIO/rmb-geomarketing.git](https://github.com/SEU-USUARIO/rmb-geomarketing.git)
