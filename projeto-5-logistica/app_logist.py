import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(layout='wide', page_title="Olist Logistics: Dados Reais")

# --- 1. Conexão com os Dados Reais ---
@st.cache_data
def carregar_dados_olist():
    """
    Carrega o dataset oficial da Olist (Brazilian E-Commerce) direto do GitHub.
    Arquivo: olist_orders_dataset.csv
    """
    # URL RAW do Repositório (Dados Públicos)
    url = "https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_orders_dataset.csv"
    
    try:
        # Carregando direto da nuvem
        df = pd.read_csv(url)
        
        # --- 2. ENGENHARIA DE DADOS (Cálculo do Lead Time) ---
        # Converter colunas de texto para Data
        cols_data = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
        for col in cols_data:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Eliminar pedidos não entregues ou cancelados
        df = df.dropna(subset=['order_delivered_customer_date', 'order_purchase_timestamp'])
        df = df[df['order_status'] == 'delivered']
        
        # CALCULAR DIAS DE ENTREGA (Lead Time Real)
        # Diferença entre Compra e Entrega
        df['Dias_Entrega'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
        
        # Calcular Atraso (Se entregou depois do estimado)
        df['Atrasado'] = df['order_delivered_customer_date'] > df['order_estimated_delivery_date']
        df['Status_Prazo'] = df['Atrasado'].apply(lambda x: 'Atrasado' if x else 'No Prazo')
        
        # Selecionar apenas colunas úteis para o dashboard
        df_final = df[['order_id', 'order_status', 'Dias_Entrega', 'Status_Prazo', 'order_purchase_timestamp']]
        
        return df_final
        
    except Exception as e:
        st.error(f"Erro ao conectar no GitHub da Olist: {e}")
        return pd.DataFrame()

# --- 3. DASHBOARD ---
st.title("Dashboard de Logística Real (baseado no Olist E-Commerce)")
st.markdown(f"""
Este painel consome dados **reais** do repositório público da Olist.
Análise focada no **Tempo de Entrega (Lead Time)** de 100k pedidos.
**Fonte:** [GitHub Olist](https://github.com/olist/work-at-olist-data)
""")

with st.spinner('Baixando base de dados real (10MB+)...'):
    df = carregar_dados_olist()

if not df.empty:
    
    # KPIs Gerais
    st.sidebar.header("Filtros")
    # Filtro de Ano para não poluir o gráfico
    anos = df['order_purchase_timestamp'].dt.year.unique()
    sel_anos = st.sidebar.multiselect("Filtrar Ano da Compra", anos, default=anos)
    
    df_filtrado = df[df['order_purchase_timestamp'].dt.year.isin(sel_anos)]
    
    # --- 4. ESTATÍSTICA DESCRITIVA ---
    st.subheader("1. Estatística Descritiva: Tempo de Entrega (Dias)")
    
    col_stats, col_raw = st.columns([1, 2])
    
    with col_stats:
        # Média, Std, Min, Max
        desc = df_filtrado['Dias_Entrega'].describe()
        
        st.markdown(f"""
        | Indicador | Valor Real |
        | :--- | :--- |
        | **Total de Pedidos** | {desc['count']:,.0f} |
        | **Média (Mean)** | **{desc['mean']:.2f} dias** |
        | **Desvio Padrão** | {desc['std']:.2f} dias |
        | **Mínimo** | {desc['min']:.0f} dias |
        | **Mediana (Q2)** | {desc['50%']:.0f} dias |
        | **Máximo** | {desc['max']:.0f} dias |
        """)
        
        if desc['max'] > 100:
            st.error("⚠️ **Outlier Extremo:** Há pedidos que levaram meses para chegar!")

    with col_raw:
        st.caption("Amostra dos Dados Brutos (Raw Data)")
        st.dataframe(
            df_filtrado.sort_values(by='Dias_Entrega', ascending=False).head(100), 
            use_container_width=True, 
            height=300
        )

    st.divider()

    # --- 5. VISUALIZAÇÃO GRÁFICA ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("2. Histograma de Prazos")
        # Histograma Real
        fig_hist = px.histogram(
            df_filtrado, 
            x="Dias_Entrega", 
            nbins=100, # Mais bins para ver a cauda longa
            title="Distribuição Real dos Prazos de Entrega",
            color_discrete_sequence=['#00a65a']
        )
        fig_hist.update_layout(yaxis_title="Quantidade de Pedidos")
        
        # Limitando o eixo X para facilitar visualização (muitos outliers de 200 dias estragam o gráfico)
        fig_hist.update_xaxes(range=[0, 60]) 
        
        media = desc['mean']
        mediana = desc['50%']
        
        # Linhas de Referência (Simplificado)
        fig_hist.add_vline(x=media, line_dash="dash", line_color="red", annotation_text=f"Média: {media:.1f}", annotation_position="top right")
        fig_hist.add_vline(x=mediana, line_dash="dot", line_color="black", annotation_text=f"Mediana: {mediana:.1f}", annotation_position="top left")
        
        st.plotly_chart(fig_hist, use_container_width=True)
        st.caption("Nota: O gráfico foi cortado em 60 dias para melhor visualização, mas a cauda longa existe.")

    with col2:
        st.subheader("3. Box Plot (Análise de Atrasos)")
        # Box Plot comparando quem atrasou vs quem chegou no prazo
        fig_box = px.box(
            df_filtrado, 
            x="Status_Prazo", 
            y="Dias_Entrega", 
            color="Status_Prazo",
            title="Dispersão: Entregas no Prazo vs. Atrasadas",
            points="outliers"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    st.info("""
    **Análise Técnica:**
    * Observar como a **Média** é maior que a **Mediana** no histograma. Isso indica uma distribuição "Assimétrica à Direita" (Right Skewed).
    * Tradução para o Negócio: A maioria das entregas é rápida, mas os poucos casos problemáticos (os *outliers* de 150+ dias) puxam a média para cima. **E é por isso (por conta dos *outliers*) que olhar só para a média é perigoso.**
    """)

else:
    st.error("Não foi possível carregar os dados. Verifique sua conexão com a internet.")