# 📊 Proyecto de Gestión de RCD (Residuos de Construcción y Demolición)

Este proyecto implementa un dashboard en **Streamlit** para la visualización, análisis y predicción de la gestión de residuos de construcción y demolición (RCD) en Antioquia.  

Se incluyen análisis descriptivos, modelos predictivos entrenados y mapas interactivos.

# 📂 Estructura del Proyecto

```bash
├── app.py                   # 🚀 Aplicación principal de Streamlit
├── requirements.txt         # 📦 Dependencias del proyecto
├── .gitignore               # 🙈 Archivos/carpetas ignorados en Git
│
├── data/                    # 📊 Datos de entrada
│   ├── Antioquia.gpkg
│   ├── datos_gestores_rcd.csv
│   ├── datos_modelo_random.csv
│   └── mapeo_municipios.csv
│
├── notebooks/               # 📓 Jupyter Notebooks (análisis y modelos)
│   ├── analysis.ipynb
│   └── ModeloPredictivo.ipynb
│
├── images/                  # 🖼️ Recursos gráficos
│   ├── aprovechamiento.png
│   ├── aprovechamientoesp.png
│   ├── generacionporsubregion.png
│   └── graficatorta.png
│
├── modules/                 # ⚙️ Módulos de análisis y utilidades
│   ├── contextProblem.py
│   ├── descriptiveAnalysis.py
│   ├── predictiveAnalysis.py
│   ├── styles.py
│   └── utils.py
│
├── predictiveModels/        # 🤖 Modelos predictivos entrenados
│   ├── modelo_concreto.pkl
│   ├── modelo_pavimento.pkl
│   ├── modelo_roca.pkl
│   ├── modelo_tierras.pkl
│   └── modelo.py
```


## ⚙️ Instalación

1. Clona el repositorio:
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>

2. crea y activa el entorno virtual:

    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows

3. Instala las dependencias:

    pip install -r requirements.txt

## ▶️ Uso
    Ejecuta la aplicación con:
        streamlit run app.py
        Esto abrirá la interfaz en tu navegador

🛠 Tecnologías utilizadas
- Python 3.10+

- Streamlit → Interfaz web interactiva

- GeoPandas / Folium → Manejo y visualización de datos geoespaciales

- Pandas / NumPy → Análisis de datos

- Scikit-learn → Modelos predictivos

- Matplotlib / Seaborn → Gráficos estadísticos

👤 Autores
Proyecto desarrollado por:
    - Tomás Acevedo Roldán
    - David Ramirez Rodriguez
    - Darwin Salgado Martínez
    - Bilman Andrés Marmolejo Palacio