import streamlit as st
import geopandas as gpd
import folium
from shapely.geometry import Point
from streamlit_folium import st_folium
from folium import GeoJson
import fiona  # para listar capas
import base64
import joblib
import pandas as pd
import numpy as np

# =========================
# Configuración de página
# =========================
st.set_page_config(
    page_title="Gestión de RCD",
    layout="wide",
    page_icon="👷🏻"
)

# =========================
# Imagen de fondo local
# =========================
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Reemplaza 'fondo.jpg' por el nombre de tu archivo local
image_path = "fotofinal.jpeg"
encoded_image = get_base64_of_bin_file(image_path)

# =========================
# Estilos CSS personalizados
# =========================
st.markdown(f"""
    <style>
    /* =========================
       Fondo con overlay
    ========================= */
    .stApp {{
        position: relative;
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        color: #212121; /* texto gris oscuro (legible) */
    }}

    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(245, 245, 245, 0.4); /* overlay gris claro */
        z-index: 0;
    }}

    .stApp > * {{
        position: relative;
        z-index: 1;
    }}

    /* =========================
       Banner
    ========================= */
    .banner {{
        background: linear-gradient(90deg, #4CAF50, #2E7D32); /* verde reciclaje */
        padding: 30px 20px;
        border-radius: 16px;
        text-align: center;
        color: #FFFFFF;
        font-size: 34px !important; /* fijo */
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    }}

    /* =========================
       Subtítulos
    ========================= */
    h2, h3, h4 {{
        color: #2E2E2E; /* gris carbón */
        margin-bottom: 20px;
        font-size: 36px !important;
        font-weight: 600;
    }}

    /* =========================
       Texto dentro de divs (excepto banner)
    ========================= */
    div:not(.banner) {{
        font-size: 22px;  /* aquí aumentas el tamaño del texto */
    }}

    /* =========================
       Pestañas
    ========================= */
    .stTabs [role="tablist"] button {{
        background-color: #E8F5E9; /* verde muy claro */
        color: #2E2E2E;
        border-radius: 12px;
        margin-right: 20px;
        padding: 24px 48px;
        font-size: 30px;
        font-weight: 800;
        border: 1px solid #C8E6C9; /* borde verde suave */
        transition: all 0.3s ease;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }}

    /* Aplica el estilo directo al texto del tab */
    .stTabs [role="tablist"] button p {{
        font-size: 22px !important;
        font-weight: 700 !important;
    }}

    .stTabs [role="tablist"] button:hover {{
        background-color: #A5D6A7; /* verde medio */
        color: #1B5E20;
    }}

    .stTabs [role="tablist"] button[aria-selected="true"] {{
        background-color: #388E3C; /* verde fuerte */
        color: #FFFFFF;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }}

    /* Contenedor de cada tab */
    div[data-baseweb="tab-panel"] {{
        background-color: rgba(255, 255, 255, 0.60);
        padding: 30px;
        margin-top: 15px;
        border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        border-left: 6px solid #4CAF50; /* detalle verde reciclaje */
    }}

    /* =========================
       Inputs y botones
    ========================= */
    input, select, button {{
        border-radius: 10px;
        border: 1px solid #BDBDBD; /* gris hormigón */
        padding: 10px 14px;
        font-size: 16px;
        transition: all 0.3s ease;
    }}

    input:focus, select:focus {{
        border-color: #4CAF50;
        box-shadow: 0 0 8px rgba(76,175,80,0.4);
        outline: none;
    }}

    button {{
        background-color: #4CAF50;
        color: #FFFFFF;
        font-weight: 600;
        cursor: pointer;
    }}

    button:hover {{
        background-color: #2E7D32;
    }}
</style>

""", unsafe_allow_html=True)

# =========================
# Banner
# =========================
st.markdown('<div class="banner">👷🏻 Análisis de Datos para la Gestión de Residuos de Construcción y Demolición (RCD) en Antioquia</div>', unsafe_allow_html=True)

# =========================
# Tabs principales
# =========================
tab1, tab2, tab3 = st.tabs(["📄 Contexto del Problema", "📊 Análisis Descriptivo", "🧠 Análisis Predictivo"])

with tab1:
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



with tab2:
    st.subheader("📊 Análisis Descriptivo")
    st.markdown("""
    El análisis exploratorio de los datos sobre los Residuos de Construcción y Demolición (RCD) en Antioquia 
    permitió identificar patrones relevantes tanto en la composición de los materiales generados, como en su 
    distribución espacial y el nivel de aprovechamiento por subregión y municipio.
    """)

    # Contenedor centrado con título arriba
    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Generación de RCD por Tipo</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Mostrar imagen centrada con st.image usando columnas
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("graficatorta.png", use_container_width=True)

    st.markdown("""
    En esta gráfica podemos ver la proporción de cada uno de los tipos de RCD que tuvimos en cuenta para 
    este análisis (Concreto, Pavimento, Roca, Tierras). La gráfica circular muestra que los RCD están compuestos 
    principalmente por tierras, seguidas por roca y concreto, mientras que el pavimento tiene una presencia mínima.
    Este patrón evidencia que la mayor parte de los RCD proviene de actividades de excavación y 
    movimientos de tierra, lo cual tiene implicaciones directas en el diseño de estrategias de aprovechamiento.
    """)

    # Contenedor centrado con título arriba
    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Distribución de los RCD por Subregión</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Mostrar imagen centrada con st.image usando columnas
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("generacionporsubregion.png", use_container_width=True)

    st.markdown("""
    El análisis por subregiones revela una alta concentración de generación de 
    RCD en el Valle de Aburrá, con predominancia de materiales tipo tierras, roca y concreto. Le siguen las 
    subregiones de Urabá y Oriente, aunque con volúmenes significativamente menores. El resto de subregiones 
    presenta una generación marginal. Este resultado se asocia directamente al grado de urbanización y actividad 
    constructiva, destacando el Valle de Aburrá como la zona crítica en términos de generación y gestión de RCD.
    """)

    # Contenedor centrado con título arriba
    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Aprovechamiento de RCD por Municipio</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Mostrar imagen centrada con st.image usando columnas
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("aprovechamiento.png", use_container_width=True)

    st.markdown("""
    El análisis por municipio muestra una gran variabilidad en el aprovechamiento de RCD. En el Valle de Aburrá 
    destacan Medellín, Copacabana e Itagüí con altos niveles de articulación con gestores autorizados, 
    mientras que otros municipios de la misma subregión presentan resultados intermedios. En el Oriente, 
    casos como El Retiro, Guarne y La Ceja reflejan un aprovechamiento parcial de la capacidad instalada, y 
    en el Norte, San Pedro de los Milagros se mantiene en un nivel medio, por debajo de los valores más altos 
    del área metropolitana.
    """)

    # Contenedor centrado con título arriba
    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <h4 style="margin-bottom: 15px;">Distribución Espacial del Aprovechamiento de RCD</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Mostrar imagen centrada con st.image usando columnas
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("aprovechamientoespacial.png", use_container_width=True)

    st.markdown("""
    El mapa de calor permite observar una concentración espacial del aprovechamiento en el área metropolitana del
    Valle de Aburrá, en especial en Medellín y sus municipios aledaños. A medida que se avanza hacia subregiones 
    periféricas, el nivel de aprovechamiento disminuye, lo que pone en evidencia una asimetría territorial en el 
    acceso a gestores autorizados. Este hallazgo confirma la necesidad de fortalecer la infraestructura y la 
    articulación logística en zonas por fuera del área metropolitana, con el fin de evitar que los residuos 
    generados allí sean dispuestos de manera inadecuada en sitios de disposición final.
    """)

with tab3:
    st.subheader("🧠 Análisis Predictivo")

    st.markdown("""
    El modelo predictivo desarrollado permite, a partir de la ubicación geográfica de una obra de construcción 
    o demolición, sugerir los gestores más adecuados para la disposición o aprovechamiento de cada tipo de RCD 
    generado.

    La herramienta se construyó mediante análisis geoespacial y un modelo de Random Forest (técnica de aprendizaje 
    automático), con el fin de optimizar la asignación de RCD, mejorar la eficiencia en la gestión, reducir los 
    impactos ambientales y apoyar la planificación territorial en Antioquia.
    """)

    # =========================
    # LÓGICA DE MAPAS (SIN CAMBIOS)
    # =========================
    ruta = "Antioquia.gpkg"

    # Listar capas disponibles
    capas = fiona.listlayers(ruta)
    print("Capas disponibles:", capas)

    # Cargar la primera capa (o la que necesites)
    gdf = gpd.read_file(ruta, layer=capas[0]).to_crs(epsg=4326)

    # Mostrar info en consola
    print("Columnas:", gdf.columns)
    print("Tipo de geometría:", gdf.geom_type.unique())
    print("CRS:", gdf.crs)

    # Lista de municipios a partir del archivo
    mapeo_municipios = pd.read_csv('mapeo_municipios.csv')
    LISTA_MUNICIPIOS = mapeo_municipios["Municipio"]


    st.markdown(
    "<b>Selecciona un municipio, ubica unas coordenadas dentro de él y calcula los residuos de construcción y demolición que se pueden aprovechar.</b>",
    unsafe_allow_html=True
    )

    municipio_sel = st.selectbox("📍 Selecciona un Municipio", sorted(LISTA_MUNICIPIOS))

    st.subheader("🌍 Mapa para seleccionar la ubicación en el municipio")

    # Filtrar municipio seleccionado (GeoDataFrame)
    mun_gdf = gdf[gdf["MpNombre"] == municipio_sel]

    # Obtener geometría y datos
    mun_geom = mun_gdf.geometry.values[0]  # MultiPolygon o Polygon
    subregion = mun_gdf["Mp_SUBREGI"].values[0]

    # Calcular centroide
    centroide = mun_geom.centroid
    centro_lat = centroide.y
    centro_lon = centroide.x

    # Mapa con municipio resaltado
    m = folium.Map(location=[centro_lat, centro_lon], zoom_start=11)

    GeoJson(
        mun_geom.__geo_interface__,
        name="Municipio",
        style_function=lambda x: {
            "fillColor": "yellow",
            "color": "red",
            "weight": 2,
            "fillOpacity": 0.2
        }
    ).add_to(m)

    col1, col2, col3 = st.columns([1, 1.8, 1])  # la del medio es más grande

    with col2:  
        map_data = st_folium(m, width=700, height=500)

    # Procesar clic y predicción
    if map_data and map_data["last_clicked"]:
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]

        punto = Point(lon, lat)

        if not mun_geom.contains(punto):
            st.error(f"❌ La ubicación seleccionada está fuera del municipio de {municipio_sel}.")

        else:
            st.success(f"🔍 Predicción para {municipio_sel} ({subregion}) en ({lat:.4f}, {lon:.4f})")

            # ================================
            # Función para cargar y usar modelos
            # ================================
            def cargar_modelo(nombre_modelo):
                """Carga un modelo entrenado desde archivo .pkl"""
                ruta = f"modelo_{nombre_modelo}.pkl"
                return joblib.load(ruta)

            def predecir(nombre_modelo, datos_nuevos):
                """Hace predicciones con el modelo especificado"""
                modelo = cargar_modelo(nombre_modelo)
                # convertir datos en DataFrame con las columnas esperadas
                X_nuevo = pd.DataFrame([datos_nuevos], columns=["Municipio", "Latitud_Y", "Longitud_X"])
                return modelo.predict(X_nuevo)[0]

            num_municipio = mapeo_municipios.loc[
                mapeo_municipios["Municipio"] == municipio_sel, "Codigo"
            ].values[0]

            punto_a_predicir = [num_municipio, lat, lon]

            pred_pavimento = predecir("pavimento", punto_a_predicir)
            pred_concreto  = predecir("concreto", punto_a_predicir)
            pred_roca      = predecir("roca", punto_a_predicir)
            pred_tierras   = predecir("tierras", punto_a_predicir)

            print("Predicciones para el nuevo punto:")
            print("Pavimento:", pred_pavimento)
            print("Concreto :", pred_concreto)
            print("Roca     :", pred_roca)
            print("Tierras  :", pred_tierras)

            # ================================
            # MAPA DE RESULTADOS
            # ================================
            mapa_pred = folium.Map(location=[lat, lon], zoom_start=11)

            # Marcar la ubicación seleccionada
            folium.Marker(
                location=[lat, lon],
                popup="Ubicación seleccionada",
                icon=folium.Icon(color="red", icon="map-marker")
            ).add_to(mapa_pred)

            ubicaciones = {}

            def agregar_gestor(cercano, color, residuo):
                key = (cercano["Y"], cercano["X"])
                if key not in ubicaciones:
                    ubicaciones[key] = []
                ubicaciones[key].append((residuo, cercano))

            dataRCD = pd.read_csv("datos_gestores_rcd.csv")

            # ================================
            # Función para encontrar el más cercano
            # ================================
            def gestor_mas_cercano(df, lat, lon):
                """Encuentra el gestor más cercano a la coordenada dada"""
                if df.empty:
                    return None

                # Calcular distancia euclidiana simple
                df = df.copy()
                df["distancia"] = np.sqrt((df["Y"] - lat)**2 + (df["X"] - lon)**2)

                # Seleccionar el más cercano
                return df.loc[df["distancia"].idxmin()]

            # =========================
            # Pavimento (PvF)
            # =========================
            if pred_pavimento:
                dataPvF = dataRCD[dataRCD['RECIBE'] == "PvF"]
                cercano = gestor_mas_cercano(dataPvF, lat, lon)
                if cercano is not None:
                    st.success(f"✅ Pavimento puede aprovecharse en: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "green", "Pavimento")
            else:
                dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
                cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
                if cercano is not None:
                    st.error(f"❌ Pavimento no puede aprovecharse. "
                            f"Llevar al centro de disposición final: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "gray", "Disposición Final (Pavimento)")

            # =========================
            # Concreto
            # =========================
            if pred_concreto:
                dataConcreto = dataRCD[dataRCD['RECIBE'] == "Concreto"]
                cercano = gestor_mas_cercano(dataConcreto, lat, lon)
                if cercano is not None:
                    st.success(f"✅ Concreto puede aprovecharse en: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "orange", "Concreto")
            else:
                dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
                cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
                if cercano is not None:
                    st.error(f"❌ Concreto no puede aprovecharse. "
                            f"Llevar al centro de disposición final: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "gray", "Disposición Final (Concreto)")

            # =========================
            # Roca/Base
            # =========================
            if pred_roca:
                dataBase = dataRCD[dataRCD['RECIBE'] == "Base"]
                cercano = gestor_mas_cercano(dataBase, lat, lon)
                if cercano is not None:
                    st.success(f"✅ Roca/Base puede aprovecharse en: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "red", "Roca/Base")
            else:
                dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
                cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
                if cercano is not None:
                    st.error(f"❌ Roca/Base no puede aprovecharse. "
                            f"Llevar al centro de disposición final: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "gray", "Disposición Final (Roca/Base)")

            # =========================
            # Tierras
            # =========================
            if pred_tierras:
                dataTierra = dataRCD[dataRCD['RECIBE'] == "Tierras"]
                cercano = gestor_mas_cercano(dataTierra, lat, lon)
                if cercano is not None:
                    st.success(f"✅ Tierras puede aprovecharse en: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "purple", "Tierras")
            else:
                dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
                cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
                if cercano is not None:
                    st.error(f"❌ Tierras no puede aprovecharse. "
                            f"Llevar al centro de disposición final: "
                            f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                            f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})")
                    agregar_gestor(cercano, "gray", "Disposición Final (Tierras)")

                    
            # --- Después de procesar todas las predicciones ---
            for (lat_g, lon_g), residuos in ubicaciones.items():
                popup_html = "<b>Gestor:</b><br>"
                for r, c in residuos:
                    popup_html += f"✅ {r} en {c['NOMBRE_RAZON_SOCIAL']} ({c['MUNICIPIO']})<br>"

                folium.Marker(
                    location=[lat_g, lon_g],
                    popup=popup_html,
                    icon=folium.Icon(color="blue", icon="industry", prefix="fa")
                ).add_to(mapa_pred)
            
            # Mostrar mapa de predicción con gestores
            st.subheader("🌍 Mapa con Ubicación Seleccionada y Gestores Sugeridos")

            col1, col2, col3 = st.columns([1, 1.8, 1])  # la del medio es más grande

            with col2:

                st_folium(mapa_pred, width=700, height=500)