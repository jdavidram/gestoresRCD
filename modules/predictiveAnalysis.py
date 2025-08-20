import streamlit as st
import geopandas as gpd
import folium
from shapely.geometry import Point
from streamlit_folium import st_folium
from folium import GeoJson
import fiona
import pandas as pd
from modules.utils import predecir, gestor_mas_cercano

def render():
    # ================================
    # Título y descripción
    # ================================
    st.subheader("🧠 Análisis Predictivo")
    st.markdown("""
    El modelo predictivo desarrollado permite, a partir de la ubicación geográfica de una obra de construcción 
    o demolición, sugerir los gestores más adecuados para la disposición o aprovechamiento de cada tipo de RCD 
    generado.

    La herramienta se construyó mediante análisis geoespacial y un modelo de Random Forest (técnica de aprendizaje 
    automático), con el fin de optimizar la asignación de RCD, mejorar la eficiencia en la gestión, reducir los 
    impactos ambientales y apoyar la planificación territorial en Antioquia.
    """)

    # ================================
    # Cargar información geoespacial
    # ================================
    ruta = "data/Antioquia.gpkg"
    capas = fiona.listlayers(ruta)  # Listar capas disponibles
    print("Capas disponibles:", capas)

    gdf = gpd.read_file(ruta, layer=capas[0]).to_crs(epsg=4326)

    # Debug en consola
    print("Columnas:", gdf.columns)
    print("Tipo de geometría:", gdf.geom_type.unique())
    print("CRS:", gdf.crs)

    # ================================
    # Municipios
    # ================================
    mapeo_municipios = pd.read_csv('data/mapeo_municipios.csv')
    LISTA_MUNICIPIOS = mapeo_municipios["Municipio"]

    st.markdown(
        "<b>Selecciona un municipio, ubica unas coordenadas dentro de él y calcula los residuos de construcción y demolición que se pueden aprovechar.</b>",
        unsafe_allow_html=True
    )

    municipio_sel = st.selectbox("📍 Selecciona un Municipio", sorted(LISTA_MUNICIPIOS))

    st.subheader("🌍 Mapa para seleccionar la ubicación en el municipio")

    # ================================
    # Filtrar municipio seleccionado
    # ================================
    mun_gdf = gdf[gdf["MpNombre"] == municipio_sel]
    mun_geom = mun_gdf.geometry.values[0]   # Geometría
    subregion = mun_gdf["Mp_SUBREGI"].values[0]

    # Calcular centroide del municipio
    centroide = mun_geom.centroid
    centro_lat, centro_lon = centroide.y, centroide.x

    # Mapa del municipio resaltado
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

    # Mostrar mapa en la app
    _, col2, _ = st.columns([1, 1.8, 1])
    with col2:
        map_data = st_folium(m, width=700, height=500)

    # ================================
    # Procesar clic en el mapa
    # ================================
    if map_data and map_data["last_clicked"]:
        lat, lon = map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"]
        punto = Point(lon, lat)

        # Validar si está dentro del municipio
        if not mun_geom.contains(punto):
            st.error(f"❌ La ubicación seleccionada está fuera del municipio de {municipio_sel}.")
            return
        else:
            st.success(f"🔍 Predicción para {municipio_sel} ({subregion}) en ({lat:.4f}, {lon:.4f})")

        # ================================
        # Preparar entrada para el modelo
        # ================================
        num_municipio = mapeo_municipios.loc[
            mapeo_municipios["Municipio"] == municipio_sel, "Codigo"
        ].values[0]
        punto_a_predicir = [num_municipio, lat, lon]

        # Predicciones
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
        # Mapa de resultados
        # ================================
        mapa_pred = folium.Map(location=[lat, lon], zoom_start=11)

        # Marcar ubicación seleccionada
        folium.Marker(
            location=[lat, lon],
            popup="Ubicación seleccionada",
            icon=folium.Icon(color="red", icon="map-marker")
        ).add_to(mapa_pred)

        # Diccionario para gestores
        ubicaciones = {}

        def agregar_gestor(cercano, residuo):
            key = (cercano["Y"], cercano["X"])
            if key not in ubicaciones:
                ubicaciones[key] = []
            ubicaciones[key].append((residuo, cercano))

        # Datos de gestores RCD
        dataRCD = pd.read_csv("data/datos_gestores_rcd.csv")

        # ================================
        # Pavimento
        # ================================
        if pred_pavimento:
            dataPvF = dataRCD[dataRCD['RECIBE'] == "PvF"]
            cercano = gestor_mas_cercano(dataPvF, lat, lon)
            if cercano is not None:
                st.success(
                    f"✅ Pavimento puede aprovecharse en: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Pavimento")
        else:
            dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
            cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
            if cercano is not None:
                st.error(
                    f"❌ Pavimento no puede aprovecharse. "
                    f"Llevar al centro de disposición final: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Disposición Final (Pavimento)")

        # ================================
        # Concreto
        # ================================
        if pred_concreto:
            dataConcreto = dataRCD[dataRCD['RECIBE'] == "Concreto"]
            cercano = gestor_mas_cercano(dataConcreto, lat, lon)
            if cercano is not None:
                st.success(
                    f"✅ Concreto puede aprovecharse en: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Concreto")
        else:
            dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
            cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
            if cercano is not None:
                st.error(
                    f"❌ Concreto no puede aprovecharse. "
                    f"Llevar al centro de disposición final: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Disposición Final (Concreto)")

        # ================================
        # Roca/Base
        # ================================
        if pred_roca:
            dataBase = dataRCD[dataRCD['RECIBE'] == "Base"]
            cercano = gestor_mas_cercano(dataBase, lat, lon)
            if cercano is not None:
                st.success(
                    f"✅ Roca/Base puede aprovecharse en: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Roca/Base")
        else:
            dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
            cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
            if cercano is not None:
                st.error(
                    f"❌ Roca/Base no puede aprovecharse. "
                    f"Llevar al centro de disposición final: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Disposición Final (Roca/Base)")

        # ================================
        # Tierra
        # ================================
        if pred_tierras:
            dataTierra = dataRCD[dataRCD['RECIBE'] == "Tierras"]
            cercano = gestor_mas_cercano(dataTierra, lat, lon)
            if cercano is not None:
                st.success(
                    f"✅ Tierras puede aprovecharse en: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Tierra")
        else:
            dataRCD_disp = dataRCD[dataRCD['RECIBE'] == "RCD"]
            cercano = gestor_mas_cercano(dataRCD_disp, lat, lon)
            if cercano is not None:
                st.error(
                    f"❌ Tierras no puede aprovecharse. "
                    f"Llevar al centro de disposición final: "
                    f"**{cercano['NOMBRE_RAZON_SOCIAL']}** "
                    f"({cercano['MUNICIPIO']}, {cercano['DIRECCION']})"
                )
                agregar_gestor(cercano, "Disposición Final (Tierra)")

        # ================================
        # Agregar gestores al mapa
        # ================================
        for (lat_g, lon_g), residuos in ubicaciones.items():
            popup_html = "<b>Gestor:</b><br>"
            for r, c in residuos:
                popup_html += f"✅ {r} en {c['NOMBRE_RAZON_SOCIAL']} ({c['MUNICIPIO']})<br>"

            folium.Marker(
                location=[lat_g, lon_g],
                popup=popup_html,
                icon=folium.Icon(color="blue", icon="industry", prefix="fa")
            ).add_to(mapa_pred)

        # Mostrar mapa de resultados
        st.subheader("🌍 Mapa con Ubicación Seleccionada y Gestores Sugeridos")
        _, col2, _ = st.columns([1, 1.8, 1])
        with col2:
            st_folium(mapa_pred, width=700, height=500)