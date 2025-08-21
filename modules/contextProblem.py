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
    "<p style='font-size:24px; font-weight:600;'>👤 Actores Clave</p>",
    unsafe_allow_html=True)
    st.markdown("""
    Esta herramienta está dirigida a diversos actores que intervienen en la gestión de los Residuos de Construcción y Demolición (RCD) en Antioquia, entre los cuales se destacan:  
    - **Autoridades ambientales**, quienes requieren información georreferenciada para la planificación y seguimiento de la disposición y aprovechamiento de RCD.  
    - **Empresas constructoras y contratistas**, que pueden usar la herramienta para identificar los gestores más adecuados según el tipo de residuo generado en cada obra.  
    - **Gestores de RCD**, para optimizar la logística de recolección, transporte y aprovechamiento de los residuos.  
    - **Investigadores y académicos**, interesados en análisis geoespaciales y modelación predictiva aplicada a la gestión de residuos.  
    """)

    st.markdown(
    "<p style='font-size:24px; font-weight:600;'>🗂️ Datos Utilizados</p>",
    unsafe_allow_html=True)
    st.markdown("""
    Los datos utilizados en este proyecto fueron recolectados por uno de los autores durante sus prácticas 
    universitarias en una empresa del sector de la construcción, lo que permitió obtener información detallada 
    sobre las ejecuciones en obra.  
    Adicionalmente, la información sobre los gestores de Residuos de Construcción y Demolición (RCD) y la información de los mapas de Antioquia 
    se obtuvo de fuentes oficiales, como el Área Metropolitana del Valle de Aburrá, CORANTIOQUIA, CORNARE y Colombia en Mapas, tal como se indica 
    en la bibliografía.
    """)

    st.markdown(
    "<p style='font-size:24px; font-weight:600;'>📚 Bibliografía</p>",
    unsafe_allow_html=True
    )

    st.markdown("""  
    - [Guía regional de procesos técnicos y jurídicos para el manejo integral de RCD](https://www.metropol.gov.co/Paginas/Noticias/nueva-guia-rcd-2023-area-metropolitana.aspx)

    **Normativa**  
    - [Resolución 0472 de 2017](https://www.minambiente.gov.co/wp-content/uploads/2021/10/resolucion-0472-de-2017.pdf)  
    - [Resolución 1257 de 2021](https://www.minambiente.gov.co/wp-content/uploads/2021/12/Resolucion-1257-de-2021.pdf)  
    - [Resolución 1257 de 2021 - anexos](https://www.minambiente.gov.co/wp-content/uploads/2021/12/Resolucion-1257-de-2021-Anexos.pdf)  
                
    **Listado de gestores de RCD**  
    - [Área Metropolitana del Valle de Aburrá - AMVA](https://www.metropol.gov.co/ambiental/residuos-solidos/Paginas/RCD.aspx)  
    - [CORANTIOQUIA](https://www.corantioquia.gov.co/wp-content/uploads/2024/07/LISTADO-DE-GESTORES-DE-RCD-version-3-07-2024.pdf)  
    - [CORNARE](https://www.cornare.gov.co/residuos/rcd/Gestores_RCD_Agosto_2024.pdf)  
    - CORPOURABÁ  

    **Colombia en mapas**  
    - [Municipios](https://www.colombiaenmapas.gov.co/)  

    **Datos Utilizados**  
    - [Listado de gestores de RCD](https://drive.google.com/file/d/1xUqjGTZZNOD78zlFCfIJat8yXoBnqz16/view?usp=sharing)  
    - [Ejecuciones en obra 2024 - 2025](https://drive.google.com/file/d/1gtcoMqzKFfErARIAscUY30C9u47sGBf_/view?usp=sharing)  
    - [Mapas de Antioquia](https://drive.google.com/file/d/1Mq4_ccQbs1S8o9z7w1men-ANZKGys778/view?usp=sharing)  

                
    **Herramientas de desarrollo**  
    - [Documentación de Python](https://docs.python.org/3/)  
    - [Documentación de Streamlit](https://docs.streamlit.io/)  
    - Inteligencias Artificiales
    """)
