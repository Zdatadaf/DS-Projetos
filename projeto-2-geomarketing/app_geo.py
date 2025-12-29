import streamlit as st
#-----------------------------------------------------
def exibir_readme(caminho_readme):
    with open(caminho_readme, "r", encoding="utf-8") as f:
        conteudo = f.read()
    with st.expander("📖 Sobre este Projeto (Documentação)", expanded=True):
        st.markdown(conteudo)
#-----------------------------------------------------
import pandas as pd
import numpy as np
import plotly.express as px
#-----------------------------------------------------
# 1. Título do App
st.title("🗺️ Geomarketing")
exibir_readme("projeto-2-geomarketing/readme.md") 
st.divider() # Uma linha para separar a explicação do dashboard real
#-----------------------------------------------------

# Configuração da Página
st.set_page_config(layout='wide', page_title="Geomarketing: Belém & Ananindeua")

# FUNÇÃO GERADORA DE DADOS (COM CORREÇÃO GEOGRÁFICA)
@st.cache_data
def gerar_dados_belem_ananindeua_v2():
    """
    Gera dados fictícios restritos às manchas urbanas reais de Belém e Ananindeua.
    Técnica: Geração baseada em Centroides de Bairros Reais com ajuste fino para evitar áreas de água.
    """
    np.random.seed(42) # Mantém a semente para reprodutibilidade
    
    # Definindo clusters (Zonas Reais)
    zonas = [
        # (Nome, Lat, Lon, Qtd_Pontos, Fator_Renda)
        # Coordenadas ajustadas para dentro da área urbana
        ("Belém Centro/Umarizal", -1.450, -48.485, 15, 2.0), # Alta Renda (Ajustado)
        ("Belém Aug. Montenegro", -1.380, -48.460, 12, 1.2), # Média Renda
        ("Icoaraci", -1.295, -48.480, 8, 0.8),               # Mista
        ("Ananindeua Centro/BR", -1.365, -48.375, 10, 1.0),  # Comercial
        ("Ananindeua Cid. Nova", -1.340, -48.410, 10, 1.1),  # Residencial Denso
    ]
    
    lista_bairros = []
    
    id_counter = 1
    for nome, lat_c, lon_c, qtd, fator_renda in zonas:
        # Gerar pontos ao redor do centroide da zona (Desvio padrão pequeno)
        # Reduzir o desvio (ex: 0.012) pode ajudar a manter os pontos mais coesos
        lats = lat_c + np.random.normal(0, 0.015, qtd) 
        lons = lon_c + np.random.normal(0, 0.015, qtd)
        
        # Gerar população e renda baseada na zona
        pops = np.random.randint(2000, 35000, qtd)
        rendas = np.random.randint(1200, 5000, qtd) * fator_renda
        
        for i in range(qtd):
            lista_bairros.append({
                'Bairro_ID': f"B_{id_counter:03d}",
                'Zona': nome,
                'Latitude': lats[i],
                'Longitude': lons[i],
                'Populacao': pops[i],
                'Renda_Media': int(rendas[i])
            })
            id_counter += 1
            
    df_pop = pd.DataFrame(lista_bairros)
    
    # 2. Gerar Lojas (Oferta) - Pegar amostra aleatória dos locais gerados acima
    indices_lojas = np.random.choice(df_pop.index, 18, replace=False)
    lojas_data = []
    
    for idx in indices_lojas:
        row = df_pop.loc[idx]
        # Deslocando levemente a loja para não ficar exatamente em cima do ponto do bairro
        lojas_data.append({
            'Loja_ID': f"LJ_{np.random.randint(100,999)}",
            'Latitude': row['Latitude'] + np.random.normal(0, 0.002),
            'Longitude': row['Longitude'] + np.random.normal(0, 0.002),
            'Faturamento': np.random.randint(60000, 250000)
        })
        
    df_lojas = pd.DataFrame(lojas_data)
    
    return df_pop, df_lojas

# Página 1: Dados Brutos 
def pagina_dados_brutos_v2():
    st.title('DADOS GEOESPACIAIS - EXPANSÃO METROPOLITANA')
    st.markdown("Base demográfica focada na Região Metropolitana de Belém (RMB).")
    
    df_pop, df_lojas = gerar_dados_belem_ananindeua_v2()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 Clusters Demográficos")
        st.dataframe(df_pop, use_container_width=True)
    with col2:
        st.subheader("🏢 Unidades Operacionais")
        st.dataframe(df_lojas, use_container_width=True)

# Página 2: Dashboard Mapa
def pagina_dashboard_v2():
    st.title('Região Metropolitana de Belém e Ananindeua')
    st.markdown("Análise de **Densidade de Consumo** na Grande Belém.")
    
    df_pop, df_lojas = gerar_dados_belem_ananindeua_v2()
    
    # Filtros
    st.sidebar.header("Filtros de Mercado")
    zona_sel = st.sidebar.multiselect("Selecionar Zona", df_pop['Zona'].unique(), default=df_pop['Zona'].unique())
    
    df_filtrado = df_pop[df_pop['Zona'].isin(zona_sel)]
    
    # Métricas Rápidas
    total_pop_visivel = df_filtrado['Populacao'].sum()
    media_renda_visivel = df_filtrado['Renda_Media'].mean()
    
    c1, c2, c3 = st.columns(3)
    c1.metric("População na Área", f"{int(total_pop_visivel):,}".replace(",", "."))
    c2.metric("Renda Média", f"R$ {media_renda_visivel:,.2f}")
    c3.metric("Lojas na Região", len(df_lojas))

    st.divider()
    
    # MAPA COM PLOTLY MAPBOX
    fig = px.scatter_mapbox(
        df_filtrado, 
        lat="Latitude", 
        lon="Longitude",
        size="Populacao",
        color="Renda_Media",
        color_continuous_scale=["#ffeba4", "#ff8c00", "#d30b0b", "#4a0404"],
        size_max=25,
        zoom=10.5,
        center={"lat": -1.38, "lon": -48.43},
        hover_name="Zona",
        hover_data=["Renda_Media", "Populacao"],
        mapbox_style="carto-positron",
        title="Distribuição de Potencial de Consumo (RMB)"
    )
    
    # Adicionar Lojas (Pontos Azuis)
    fig.add_scattermapbox(
        lat=df_lojas["Latitude"],
        lon=df_lojas["Longitude"],
        mode='markers',
        marker=dict(size=14, color='blue', symbol='circle'),
        text=df_lojas["Loja_ID"],
        name="Lojas Físicas"
    )
    
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0}, height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("**Legenda:** Círculos **Quentes (Vermelhos)** indicam alta renda. Pontos **Azuis** são as lojas atuais.")

# Navegação
st.sidebar.title('Navegação')
pagina = st.sidebar.radio('Ir para:', ['Mapa Analítico', 'Base de Dados'])

if pagina == 'Base de Dados':
    pagina_dados_brutos_v2()
else:
    pagina_dashboard_v2()
