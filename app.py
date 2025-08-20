import streamlit as st
from modules import styles, contextProblem, descriptiveAnalysis, predictiveAnalysis

# =========================
# Configuración de página
# =========================
st.set_page_config(
    page_title="Gestión de RCD",
    layout="wide",
    page_icon="👷🏻"
)

# =========================
# Cargar estilos
# =========================
styles.load_styles("images/fondoweb.png")

# =========================
# Banner principal
# =========================
st.markdown(styles.banner("👷🏻 Análisis de Datos para la Gestión de Residuos de Construcción y Demolición (RCD) en Antioquia"), unsafe_allow_html=True)

# =========================
# Tabs principales
# =========================
tab1, tab2, tab3 = st.tabs(["📄 Contexto del Problema", "📊 Análisis Descriptivo", "🧠 Análisis Predictivo"])

# =========================
# Contenido en cada tab
# =========================
with tab1:
    contextProblem.render()
with tab2:
    descriptiveAnalysis.render()
with tab3:
    predictiveAnalysis.render()