import streamlit as st

# 1. Configuração inicial
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. CABEÇALHO NO TOPO DA PÁGINA (Aparecerá acima de todos os projetos)
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Danilo Azevedo Figueiredo")
    st.markdown("### Cientista de Dados")
    st.caption("Especialista em Engenharia de Automação e MBA em Data Science & Analytics")

with col2:
    # Alinhando os botões à direita para ficar elegante
    st.write("") # Espaçador para alinhar verticalmente
    st.markdown(f"""
        <div style="text-align: right;">
            <a href="https://www.linkedin.com/in/danilo-a-fig" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="margin-bottom: 5px;"></a>
            <a href="https://github.com/Zolinad" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 3. DEFINIÇÃO DA NAVEGAÇÃO
pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"),
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"),
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"),
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"),
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"),
])

# 4. EXECUTAR O PROJETO ESCOLHIDO (Aparecerá abaixo do cabeçalho)
pg.run()
