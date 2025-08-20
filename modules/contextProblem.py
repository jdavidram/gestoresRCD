import streamlit as st

def render():
    st.subheader("📄 Contexto del Problema")

    st.markdown(
    "<p style='font-size:24px; font-weight:600;'>📝 Resumen</p>",
    unsafe_allow_html=True)
    st.markdown("""
    En el Valle de Aburrá se generan diariamente 18.779 toneladas de Residuos de Construcción y Demolición (RCD), 
    de las cuales solo el 2% es aprovechado, lo que constituye un desafío crítico para la sostenibilidad ambiental 
    del territorio. Este proyecto propone una estrategia integral de gestión de RCD en Antioquia, basada en el 
    análisis geoespacial de los gestores existentes y en la información recolectada sobre obras de construcción y 
    demolición en todo el departamento. El objetivo es identificar áreas de cobertura, zonas de aprovechamiento y 
    regiones destinadas a disposición final. Adicionalmente, se desarrolló una herramienta predictiva que, a partir 
    de la ubicación de una obra, sugiere los gestores adecuados para la disposición de cada tipo de RCD generado. 
    La propuesta busca fortalecer la planificación territorial, optimizar la gestión de residuos y contribuir al 
    cumplimiento de la meta departamental de aprovechamiento al 2030.
    """)

    st.markdown(
    "<p style='font-size:24px; font-weight:600;'>📖 Introducción</p>",
    unsafe_allow_html=True)
    st.markdown("""
    La generación masiva de RCD en el Valle de Aburrá, con cifras que superan las 18.700 toneladas diarias, 
    según la Guía regional con los procesos técnicos y jurídicos para el manejo integral de RCD, ha generado un 
    desafío ambiental y logístico de gran escala, convirtiendo estos residuos en uno de los principales 
    contaminantes de los ecosistemas urbanos y periurbanos. A pesar de su potencial de reutilización, solo el 
    2% es actualmente aprovechado, mientras que el resto se dispone en cuerpos de agua, puntos críticos o sitios 
    autorizados, generando impactos ambientales significativos. En respuesta, se ha formulado una estrategia 
    integral que combina análisis territorial, modelación predictiva y herramientas de planificación para mejorar 
    la eficiencia en la gestión de RCD en Antioquia.
    """)

    st.markdown(
    "<p style='font-size:24px; font-weight:600;'>🚧 Problema Impactado</p>",
    unsafe_allow_html=True)
    st.markdown("""
    El bajo porcentaje de aprovechamiento de los RCD (2%) representa una pérdida significativa de recursos 
    reutilizables y una amenaza directa para los ecosistemas del Valle de Aburrá. La disposición inadecuada de 
    estos residuos contribuye a la contaminación de cuerpos de agua, la degradación del paisaje urbano y la 
    obstrucción de cauces naturales. Además, la falta de información georreferenciada sobre los gestores limita 
    la capacidad de planificación y respuesta de las autoridades ambientales.
    """)

    st.markdown(
    "<p style='font-size:24px; font-weight:600; margin-bottom:10px;'>🎯 Objetivos Generales</p>",
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <ul style="font-size:22px; line-height:1.8; list-style-type: disc; padding-left: 20px;">
            <li>Identificar <b>áreas de cobertura</b> de los gestores.</li>
            <li>Reconocer <b>zonas óptimas</b> para el aprovechamiento y la disposición final.</li>
            <li>Desarrollar una <b>herramienta predictiva</b> que modele el porcentaje de aprovechamiento según la ubicación del proyecto y el tipo de RCD generado.</li>
            <li>Fortalecer la <b>toma de decisiones</b> en obras civiles y actividades conexas.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    "<p style='font-size:24px; font-weight:600; margin-bottom:10px;'>📑 Marco Normativo Vigente</p>",
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <ul style="font-size:22px; line-height:1.8; list-style-type: disc; padding-left: 20px;">
            <li><b>Resolución 0472 de 2017</b>: Establece los lineamientos para la gestión de RCD a nivel nacional.</li>
            <li><b>Resolución 1257 de 2021</b>: Modifica y complementa la anterior, incorporando requisitos específicos para el aprovechamiento y disposición.</li>
            <li><b>Decreto 1077 de 2015</b>: Compila normas sobre servicios públicos domiciliarios, incluyendo residuos sólidos.</li>
        </ul>

        <p style="font-size:16px; line-height:1.8; margin-top:10px;">
        En Antioquia, las autoridades ambientales como <b>Corantioquia</b>, <b>Cornare</b> y el <b>Área Metropolitana del Valle de Aburrá</b> han adoptado guías regionales que promueven el <b>aprovechamiento del 55% de los RCD para 2030</b>.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    "<p style='font-size:24px; font-weight:600;'>📚 Bibliografía</p>",
    unsafe_allow_html=True
    )

    st.markdown("""  
    - [Guía regional de procesos técnicos y jurídicos para el manejo integral de RCD](URL_AQUI)

    **Normativa**  
    - [Resolución 0472 de 2017](URL_AQUI)  
    - [Resolución 1257 de 2021](URL_AQUI)  
    - [Resolución 1257 de 2021 - anexos](URL_AQUI)  
    - [Listado de gestores de RCD](URL_AQUI)  

    **Entidades ambientales**  
    - [Área Metropolitana del Valle de Aburrá - AMVA](URL_AQUI)  
    - [CORANTIOQUIA](URL_AQUI)  
    - [CORNARE](URL_AQUI)  
    - [CORPOURABÁ](URL_AQUI)  

    **Colombia en mapas**  
    - [Municipios](URL_AQUI)  

    **Datos**  
    - [Listado de gestores de RCD](URL_AQUI)  
    - [Ejecuciones en obra](URL_AQUI)  
    - [Servicio de gas](URL_AQUI)  

    **Herramienta de desarrollo**  
    - [Documentación de Python](https://docs.python.org/3/)  
    - [Documentación de Streamlit](https://docs.streamlit.io/)  
    - Inteligencias Artificiales
    """)
