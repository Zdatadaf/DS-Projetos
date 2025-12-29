# Logística: Estatísticas do Tempo de Entrega


## Sobre o Projeto
Este projeto realiza uma **Análise Exploratória de Dados (EDA)** focada em métricas logísticas, especificamente no *Lead Time* (tempo de entrega).

Utilizando dados sintéticos baseados em datasets reais de E-Commerce, o sistema calcula estatísticas descritivas fundamentais (Média, Desvio Padrão, Quartis) e visualiza a distribuição dos dados para identificar ineficiências operacionais.

## Funcionalidades
* **Tabela Estatística Dinâmica:** Replicação visual do comando `describe()` do Pandas, apresentando métricas de tendência central e dispersão em tempo real.
* **Histograma Anotado:** Visualização da frequência de prazos com linhas verticais destacando a Média e a Mediana para identificar assimetrias (Skewness).
* **Box Plot (Diagrama de Caixa):** Ferramenta crucial para visualização de **Outliers** (valores discrepantes), segmentados por prioridade de envio.

## Lógica e Aplicabilidade (Transfer Learning)
O domínio de estatística descritiva e análise de distribuição é vital para qualquer operação que dependa de prazos e regularidade:

1.  **Logística Privada:** Análise de SLA de transportadoras.
2.  **Manutenção:** Tempo médio para reparo (MTTR) de equipamentos.
3.  **Gestão Pública (Educação):**
    * Análise de regularidade na **distribuição de Merenda Escolar** (identificando escolas que recebem fora do prazo).
    * Monitoramento de **Transporte Escolar** (variação nos horários de chegada dos ônibus).
    * Auditoria de tempo de resposta para solicitações de manutenção predial nas escolas.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Frontend:** Streamlit
* **Visualização:** Plotly Express / Graph Objects
* **Estatística:** Pandas / NumPy

