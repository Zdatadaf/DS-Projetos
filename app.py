import streamlit as st

# 1. Configuração inicial
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. CONTEÚDO NO TOPO ABSOLUTO (Usando a Sidebar manualmente)
with st.sidebar:
    st.title("Danilo Azevedo Figueiredo") [cite: 1]
    st.write("Cientista de Dados") [cite: 2]
    
    # Badges de contato imediatamente abaixo do nome
    st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-a-fig)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zolinad)
    """) [cite: 4, 6]
    
    st.divider()
    st.markdown("### Navegação do Portfólio 👇")

# 3. DEFINIÇÃO DAS PÁGINAS
# O segredo aqui é o parâmetro position="sections" ou ocultar o título do st.navigation
pg = st.navigation({
    " ": [ # Usar um espaço em branco como título de seção "esconde" o cabeçalho do menu
        st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"), [cite: 37]
        st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"), [cite: 38]
        st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"), [cite: 39]
        st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"), [cite: 40]
        st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"), [cite: 41]
    ]
})

# 4. EXECUÇÃO
pg.run()
