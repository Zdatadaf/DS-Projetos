import streamlit as st

# 1. Configuração inicial
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. DEFINIÇÃO DA NAVEGAÇÃO (Menu lateral limpo)
pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
])

# 3. EXECUTAR O CONTEÚDO DA PÁGINA SELECIONADA
pg.run()

# 4. RODAPÉ FIXO (Aparecerá no final de todas as páginas)
st.divider()
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"**Danilo Azevedo Figueiredo** | Cientista de Dados")
    st.caption("Portfólio de Projetos Aplicados - Foco em Machine Learning e Business Intelligence")

with col2:
    # Contatos alinhados à direita
    st.markdown(f"""
        <div style="text-align: right;">
            <a href="https://www.linkedin.com/in/danilo-a-fig"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="margin-bottom: 5px;"></a>
            <a href="https://github.com/Zolinad"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
        </div>
    """, unsafe_allow_html=True)
