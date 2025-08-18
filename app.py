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
from folium.plugins import MarkerCluster

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
        font-size: 20px;  /* aquí aumentas el tamaño del texto */
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
    st.subheader("Contexto del Problema")
    st.markdown("""
    El manejo de los **Residuos de Construcción y Demolición (RCD)** en Antioquia es un reto 
    que requiere de herramientas tecnológicas para predecir la generación y optimizar su gestión.
    
    Este proyecto utiliza datos geográficos y técnicas de machine learning para identificar 
    patrones de generación de RCD y apoyar la toma de decisiones en las subregiones del departamento.
    """)

with tab2:
    st.subheader("Análisis Descriptivo")
    st.markdown("""
    Aquí se presentará un análisis exploratorio de los datos, incluyendo distribuciones, 
    mapas de calor y otras visualizaciones relevantes.
    
    *(Puedes añadir gráficos o tablas descriptivas aquí)*.
    """)
    st.write("Aquí irían tus resultados de predicción.")

with tab3:
    st.subheader("🧠 Análisis Predictivo")

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

    st.markdown("Selecciona un municipio, ubica unas coordenadas dentro de él y calcula los residuos de construcción y demolición que se pueden aprovechar.")

    municipio_sel = st.selectbox("📍 Selecciona Municipio", sorted(LISTA_MUNICIPIOS))

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

    # Mostrar mapa y capturar clic
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

            # -----------------------------
            # Añadir puntero en el mapa principal
            # -----------------------------
            folium.Marker(
                location=[lat, lon],
                popup="Ubicación seleccionada",
                icon=folium.Icon(color="blue", icon="map-marker")
            ).add_to(m)

            # Renderizar mapa con puntero
            st_folium(m, width=700, height=500)


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
            st_folium(mapa_pred, width=700, height=500)