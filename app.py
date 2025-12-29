import streamlit as st

# 1. Configuração inicial
st.set_page_config(layout="wide", page_title="Portfólio de Data Science - Danilo A. F.")

# 2. CABEÇALHO COM ALINHAMENTO VERTICAL CORRIGIDO
# O parâmetro vertical_alignment="center" garante que os botões fiquem centralizados com o texto
col1, col2 = st.columns([3, 1], vertical_alignment="center")

with col1:
    st.markdown("## Danilo Azevedo Figueiredo") # [cite: 1]
    st.markdown("#### Cientista de Dados") # [cite: 2]
    st.caption("Engenheiro de Automação | MBA em Data Science & Analytics") # [cite: 8, 44]

with col2:
    # Removido o st.write("") anterior para não empurrar os botões erradamente
    st.markdown(f"""
        <div style="text-align: right;">
            <a href="https://www.linkedin.com/in/danilo-a-fig" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="margin-bottom: 5px; height: 28px;"></a>
            <a href="https://github.com/Zolinad" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" style="height: 28px;"></a>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 3. NAVEGAÇÃO E EXECUÇÃO
pg = st.navigation([
    st.Page("projeto-1-churn/app_churn.py", title="1. Predição de Churn", icon="👥"), # [cite: 37]
    st.Page("projeto-2-geomarketing/app_geo.py", title="2. Geomarketing", icon="🗺️"), # [cite: 38]
    st.Page("projeto-3-auditoria/app_audit.py", title="3. Auditoria Financeira", icon="🛡️"), # [cite: 39]
    st.Page("projeto-4-dashboard-kpi/app_kpi.py", title="4. Dashboard Estratégico", icon="📈"), # [cite: 40]
    st.Page("projeto-5-logistica/app_logist.py", title="5. Logística Real", icon="📦"), # [cite: 41]
])

pg.run()
