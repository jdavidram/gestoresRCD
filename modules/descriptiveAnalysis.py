import streamlit as st

def render():
    st.subheader("📊 Análisis Descriptivo")
    st.markdown("""
    El análisis exploratorio de los datos sobre los Residuos de Construcción y Demolición (RCD) en Antioquia 
    permitió identificar patrones relevantes tanto en la composición de los materiales generados, como en su 
    distribución espacial y el nivel de aprovechamiento por subregión y municipio.
    """)

    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Generación de RCD por Tipo</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, col2, _ = st.columns([1,2,1])
    with col2:
        st.image("images/graficatorta.png", use_container_width=True)

    st.markdown("""
    En esta gráfica podemos ver la proporción de cada uno de los tipos de RCD que tuvimos en cuenta para 
    este análisis (Concreto, Pavimento, Roca, Tierras). La gráfica circular muestra que los RCD están compuestos 
    principalmente por tierras, seguidas por roca y concreto, mientras que el pavimento tiene una presencia mínima.
    Este patrón evidencia que la mayor parte de los RCD proviene de actividades de excavación y 
    movimientos de tierra, lo cual tiene implicaciones directas en el diseño de estrategias de aprovechamiento.
    """)

    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Distribución de las Obras RCD por Subregión</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, col2, _ = st.columns([1,2,1])
    with col2:
        st.image("images/generacionporsubregion.png", use_container_width=True)

    st.markdown("""
    El análisis por subregiones revela una alta concentración de generación de 
    RCD en el Valle de Aburrá, con predominancia de materiales tipo tierras, roca y concreto. Le siguen las 
    subregiones de Urabá y Oriente, aunque con volúmenes significativamente menores. El resto de subregiones 
    presenta una generación marginal. Este resultado se asocia directamente al grado de urbanización y actividad 
    constructiva, destacando el Valle de Aburrá como la zona crítica en términos de generación y gestión de RCD.
    """)

    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Aprovechamiento de RCD por Municipio</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, col2, _ = st.columns([1,2,1])
    with col2:
        st.image("images/aprovechamiento.png", use_container_width=True)

    st.markdown("""
    El análisis por municipio muestra una gran variabilidad en el aprovechamiento de RCD. En el Valle de Aburrá 
    destacan Medellín, Copacabana e Itagüí con altos niveles de articulación con gestores autorizados, 
    mientras que otros municipios de la misma subregión presentan resultados intermedios. En el Oriente, 
    casos como El Retiro, Guarne y La Ceja reflejan un aprovechamiento parcial de la capacidad instalada, y 
    en el Norte, San Pedro de los Milagros se mantiene en un nivel medio, por debajo de los valores más altos 
    del área metropolitana.
    """)

    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Distribución Espacial del Aprovechamiento de RCD</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, col2, _ = st.columns([1,2,1])
    with col2:
        st.image("images/aprovechamientoespacial.png", use_container_width=True)

    st.markdown("""
    El mapa de calor permite observar una concentración espacial del aprovechamiento en el área metropolitana del
    Valle de Aburrá, en especial en Medellín y sus municipios aledaños. A medida que se avanza hacia subregiones 
    periféricas, el nivel de aprovechamiento disminuye, lo que pone en evidencia una asimetría territorial en el 
    acceso a gestores autorizados. Este hallazgo confirma la necesidad de fortalecer la infraestructura y la 
    articulación logística en zonas por fuera del área metropolitana, con el fin de evitar que los residuos 
    generados allí sean dispuestos de manera inadecuada en sitios de disposición final.
    """)