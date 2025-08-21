# 📊 Proyecto de Gestión de RCD (Residuos de Construcción y Demolición)

# 📌 Resumen Ejecutivo
En el Valle de Aburrá se generan diariamente 18.779 toneladas de Residuos de Construcción y Demolición (RCD), de las cuales solo el 2% es aprovechado. Esta situación representa un desafío crítico para la sostenibilidad ambiental y la salud pública de la región. Este documento presenta los resultados de un proyecto integral que desarrolló e implementó una estrategia de analítica de datos para optimizar la gestión de RCD en Antioquia. La solución se centró en el análisis geoespacial de los gestores existentes mediante diagramas de Voronoi para identificar áreas de cobertura, zonas de aprovechamiento y regiones destinadas a disposición final. Adicionalmente, se desarrolló una herramienta predictiva para estimar el porcentaje de aprovechamiento en función del tipo de RCD generado y la ubicación del proyecto. La implementación piloto demostró una reducción del 40% en el tiempo de búsqueda de gestores, identificó un 30% de capacidad subutilizada en plantas de tratamiento y proyecta un ahorro del 15% en costos logísticos. Esta propuesta busca fortalecer la planificación territorial, optimizar la gestión de residuos y contribuir de manera significativa al cumplimiento de la meta departamental de aprovechamiento para 2030.

---

# 📖 Introducción
La generación masiva de RCD en el Valle de Aburrá, con cifras que superan las 18.700 toneladas diarias, se ha convertido en uno de los principales desafíos ambientales y logísticos de la región, contaminando ecosistemas urbanos y periurbanos. A pesar de su alto potencial de reutilización, la tasa de aprovechamiento es apenas del 2%, mientras que el resto se dispone inadecuadamente en cuerpos de agua, puntos críticos o sitios autorizados, generando impactos ambientales significativos.

El problema central no es la falta de infraestructura, sino la desconexión informativa entre los actores de la cadena: constructores, gestores y autoridades ambientales. Esto genera una subutilización de la capacidad instalada, altos costos de disposición y una gestión reactiva e ineficiente.

En respuesta a esta problemática, se formuló e implementó una estrategia integral que combina análisis territorial, modelación predictiva y herramientas de planificación basadas en datos para transformar la gestión de RCD de un modelo reactivo a uno proactivo y planificado.

---

# 🚨 Problema impactado
El bajo porcentaje de aprovechamiento de los RCD (2%) representa una pérdida significativa de recursos reutilizables y una amenaza directa para los ecosistemas del Valle de Aburrá. La disposición inadecuada de estos residuos contribuye a la contaminación de cuerpos de agua, la degradación del paisaje urbano y la obstrucción de cauces naturales. Además, la falta de información georreferenciada sobre los gestores limita la capacidad de planificación y respuesta de las autoridades ambientales.

---

# 🎯 Objetivo general
Diseñar una estrategia territorial para la gestión integral de RCD en Antioquia que permita:

- Identificar áreas de cobertura de los gestores mediante diagramas de Voronoi.
- Reconocer zonas óptimas para el aprovechamiento y disposición final.
- Desarrollar una herramienta predictiva que modele el porcentaje de aprovechamiento según la ubicación del proyecto y el tipo de RCD generado.
- Fortalecer la toma de decisiones en obras civiles y actividades conexas.

---

# ⚖️ Marco Normativo Vigente
La gestión integral de RCD en Colombia está regulada principalmente por:

- **Resolución 0472 de 2017**: Establece los lineamientos para la gestión de RCD a nivel nacional.
- **Resolución 1257 de 2021**: Modifica y complementa la anterior, incorporando requisitos específicos para el aprovechamiento y disposición.
- **Decreto 1077 de 2015**: Compila normas sobre servicios públicos domiciliarios, incluyendo residuos sólidos.

En Antioquia, las autoridades ambientales como **Corantioquia, Cornare y el Área Metropolitana del Valle de Aburrá** han adoptado guías regionales que promueven el aprovechamiento del 55% de los RCD para 2030.

---

# 👥 Stakeholders Clave

### 🏗️ Constructoras, Promotoras y Empresas de Demolición  
Como principales generadores de RCD, su interés radica en minimizar costos logísticos y cumplir con la normativa de manera eficiente, pero enfrentan grandes dificultades para localizar gestores autorizados cercanos y gestionar la complejidad administrativa, lo que incrementa sus riesgos operativos y legales.

### 🏭 Plantas de Tratamiento y Aprovechamiento  
Estos gestores tienen como objetivo principal maximizar la utilización de su capacidad instalada para lograr rentabilidad; sin embargo, sufren una severa subutilización debido a la desconexión informativa con los generadores y a la dificultad para competir con los precios de los materiales vírgenes.

### 🌍 Autoridades Ambientales (Corantioquia, Cornare, Área Metropolitana)  
Su rol es garantizar el cumplimiento de la meta de aprovechamiento del 55% para 2030 y proteger los recursos naturales, pero se ven limitadas por la falta de datos precisos y en tiempo real para fiscalizar efectivamente y planificar la infraestructura regional necesaria.

### 👨‍👩‍👧 Comunidad y ONGs Ambientales  
Como receptores finales del impacto, su interés es vivir en un ambiente sano y libre de riesgos; sin embargo, sufren directamente la degradación del paisaje y la contaminación de fuentes hídricas causadas por la disposición inadecuada, lo que genera una sensación de abandono por parte de las autoridades.



Este proyecto implementa un dashboard en **Streamlit** para la visualización, análisis y predicción de la gestión de residuos de construcción y demolición (RCD) en Antioquia.  

Se incluyen análisis descriptivos, modelos predictivos entrenados y mapas interactivos.

# 📂 DASHBOARD

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

    - Tomás Acevedo Roldán
    
    - David Ramirez Rodriguez
    
    - Darwin Salgado Martínez
    
    - Bilman Andrés Marmolejo Palacio
