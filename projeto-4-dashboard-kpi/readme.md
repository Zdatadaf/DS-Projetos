# Dashboard Estratégico para Vendas: monitoramento de KPI's


## Sobre o Projeto
Este projeto é um **Dashboard Executivo** desenvolvido para monitoramento de KPIs (Key Performance Indicators) de uma rede varejista nacional.

O objetivo é democratizar o acesso aos dados, permitindo que gestores analisem a performance hierárquica (Região > Categoria) e identifiquem correlações entre **Volume de Vendas** e **Qualidade da Margem**.

O sistema simula uma arquitetura de Business Intelligence (BI) completa, com geração de dados sintéticos, ETL em tempo real e visualização interativa.

## Funcionalidades
* **Cálculo de KPIs em Tempo Real:** Faturamento, Lucro Líquido e Score de Qualidade (Margem ponderada).
* **Filtros Hierárquicos:** Drill-down dinâmico por Região e Categoria de produto.
* **Matriz de Desempenho:** Gráfico de dispersão (Scatter Plot) que cruza Volume vs. Qualidade, identificando produtos "Vaca Leiteira" (vendem muito, lucram muito) e "Abacaxis" (vendem muito, lucram pouco).
* **Indicadores de Meta:** Visualização clara de desvios em relação às metas estabelecidas (ex: Linha de corte de qualidade).

## Lógica e Aplicabilidade (Transfer Learning)
A estrutura hierárquica e os indicadores de performance deste dashboard são diretamente aplicáveis ao **Setor Educacional e Políticas Públicas**:

1.  **Monitoramento do IDEB/SAEB:**
    * Substituir "Vendas" por "Número de Matriculados".
    * Substituir "Lucro/Score" por "Nota Média na Prova".
    * Substituir "Categoria" por "Disciplinas (Matemática/Português)".
2.  **Gestão Hierárquica:** A mesma lógica de drill-down (Região -> Loja) aplica-se a (Distrito -> Escola -> Turma).
3.  **Avaliação de Políticas:** A Matriz de Desempenho serve para identificar escolas que precisam de intervenção pedagógica prioritária (Alta matrícula, baixo desempenho).

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Frontend:** Streamlit
* **Visualização:** Plotly Express
* **Manipulação de Dados:** Pandas / NumPy


