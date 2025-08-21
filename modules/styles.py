import base64
import streamlit as st

def get_base64_of_bin_file(bin_file: str) -> str:
    """Convierte una imagen en base64 para usarla como fondo."""
    with open(bin_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def load_styles(image_path: str):
    """Carga el CSS de estilos y define el fondo con overlay."""
    encoded_image = get_base64_of_bin_file(image_path)

    css = f"""
    <style>
        /* =========================
        Fondo con overlay general
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

        /* Capa de overlay encima del fondo */
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

        /* Contenido por encima del overlay */
        .stApp > * {{
            position: relative;
            z-index: 1;
        }}

        /* =========================
        Banner principal
        ========================= */
        .banner {{
            background: linear-gradient(90deg, #4CAF50, #2E7D32); /* degradado verde reciclaje */
            padding: 30px 20px;
            border-radius: 16px;
            text-align: center;
            color: #FFFFFF;
            font-size: 34px !important; /* tamaño fijo del texto */
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            margin-bottom: 25px;
        }}

        /* =========================
        Subtítulos (h2, h3, h4)
        ========================= */
        h2, h3, h4 {{
            color: #2E2E2E; /* gris carbón */
            margin-bottom: 20px;
            font-size: 36px !important;
            font-weight: 600;
        }}

        /* =========================
        Texto dentro de divs (excepto el banner)
        ========================= */
        div:not(.banner) {{
            font-size: 22px; /* aumenta tamaño de fuente */
        }}

        /* =========================
        Pestañas (tabs)
        ========================= */
        /* Botones de pestañas */
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

        /* Texto dentro de los tabs */
        .stTabs [role="tablist"] button p {{
            font-size: 22px !important;
            font-weight: 700 !important;
        }}

        /* Hover en pestañas */
        .stTabs [role="tablist"] button:hover {{
            background-color: #A5D6A7; /* verde medio */
            color: #1B5E20;
        }}

        /* Pestaña activa */
        .stTabs [role="tablist"] button[aria-selected="true"] {{
            background-color: #388E3C; /* verde fuerte */
            color: #FFFFFF;
            font-weight: 600;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }}

        /* Contenedor de contenido de cada tab */
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

        /* Efecto al enfocar inputs/select */
        input:focus, select:focus {{
            border-color: #4CAF50;
            box-shadow: 0 0 8px rgba(76,175,80,0.4);
            outline: none;
        }}

        /* Botones */
        button {{
            background-color: #4CAF50;
            color: #FFFFFF;
            font-weight: 600;
            cursor: pointer;
        }}

        /* Hover en botones */
        button:hover {{
            background-color: #2E7D32;
        }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

def banner(text: str) -> str:
    """Genera un banner estilizado con texto centrado."""
    return f"""
    <div class="banner">{text}</div>
    """