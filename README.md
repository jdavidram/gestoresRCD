<table border=1 border-collapse="collapse" width="100%">
  <thead>
    <th>
      <img src="https://static.wikia.nocookie.net/logopedia/images/5/52/EPM2007.png/revision/latest?cb=20210505181105&path-prefix=es" width="320px" height="270px" />
    </th>
    <th>
      <h1>Análisis de Datos para la Gestión de Residuos de Construcción y Demolición (RCD) en Antioquia</h1>
    </th>
  </thead>
</table>

> **Resumen**
>
> En el Valle de Aburrá se generan diariamente 18.779 toneladas de Residuos de Construcción y Demolición (RCD), de las cuales solo el 2% es aprovechado, lo que representa un desafío crítico para la sostenibilidad ambiental del territorio. Este artículo presenta una estrategia para la gestión integral de RCD en Antioquia, basada en el análisis geoespacial de los gestores existentes mediante diagramas de Voronoi, con el fin de identificar áreas de cobertura, zonas de aprovechamiento y regiones destinadas a disposición final. Además, se desarrolló una herramienta predictiva que permite estimar el porcentaje de aprovechamiento en función del tipo de RCD generado y la ubicación del proyecto. La propuesta busca fortalecer la planificación territorial, optimizar la gestión de residuos y contribuir al cumplimiento de la meta departamental de aprovechamiento para 2030.

## Introducción

La generación masiva de RCD en el Valle de Aburrá, con cifras que superan las 18.700 toneladas diarias, según la [Guía regional con los procesos técnicos y jurídicos para el manejo integral de RCD](https://www.metropol.gov.co/Paginas/Noticias/nueva-guia-rcd-2023-area-metropolitana.aspx), ha generado un desafío ambiental y logístico de gran escala, convirtiendo estos residuos en uno de los principales contaminantes de los ecosistemas urbanos y periurbanos. A pesar de su potencial de reutilización, solo el 2% es actualmente aprovechado, mientras que el resto se dispone en cuerpos de agua, puntos críticos o sitios autorizados, generando impactos ambientales significativos. En respuesta, se ha formulado una estrategia integral que combina análisis territorial, modelación predictiva y herramientas de planificación para mejorar la eficiencia en la gestión de RCD en Antioquia.

## Problema impactado

El bajo porcentaje de aprovechamiento de los RCD (2%) representa una pérdida significativa de recursos reutilizables y una amenaza directa para los ecosistemas del Valle de Aburrá. La disposición inadecuada de estos residuos contribuye a la contaminación de cuerpos de agua, la degradación del paisaje urbano y la obstrucción de cauces naturales. Además, la falta de información georreferenciada sobre los gestores limita la capacidad de planificación y respuesta de las autoridades ambientales.

## Objetivo general

Diseñar una estrategia territorial para la gestión integral de RCD en Antioquia que permita:

* Identificar áreas de cobertura de los gestores mediante diagramas de Voronoi.

* Reconocer zonas óptimas para el aprovechamiento y disposición final.

* Desarrollar una herramienta predictiva que modele el porcentaje de aprovechamiento según la ubicación del proyecto y el tipo de RCD generado.

* Fortalecer la toma de decisiones en obras civiles y actividades conexas.

# Marco Normativo Vigente

La gestión integral de RCD en Colombia está regulada principalmente por:

* Resolución 0472 de 2017: Establece los lineamientos para la gestión de RCD a nivel nacional.

* Resolución 1257 de 2021: Modifica y complementa la anterior, incorporando requisitos específicos para el aprovechamiento y disposición.

* Decreto 1077 de 2015: Compila normas sobre servicios públicos domiciliarios, incluyendo residuos sólidos.

* En Antioquia, las autoridades ambientales como Corantioquia, Cornare y el Área Metropolitana del Valle de Aburrá han adoptado guías regionales que promueven el aprovechamiento del 55% de los RCD para 2030.

## Stakeholders Clave
Los principales actores identificados son:
**Constructores:** Tienen dificultades para localizar gestores autorizados cercanos y enfrentan altos costos de disposición.
**Gestores de RCD:** Subutilizan su capacidad instalada debido a la falta de vinculación efectiva con las obras.
**Autoridades ambientales:** Carecen de datos precisos para fiscalizar y planificar infraestructura de gestión de RCD.
**Comunidad:** Sufre los efectos de la contaminación y los riesgos asociados a los botaderos ilegales.

## Bibliografia

* [Guía regional con los procesos técnicos y jurídicos para el manejo integral de RCD](https://www.metropol.gov.co/Paginas/Noticias/nueva-guia-rcd-2023-area-metropolitana.aspx)

**Normativa**

* [Resolución 0472 de 2017](https://www.minambiente.gov.co/wp-content/uploads/2021/10/resolucion-0472-de-2017.pdf)
* [Resolución 1257 de 2021](https://www.minambiente.gov.co/wp-content/uploads/2021/12/Resolucion-1257-de-2021.pdf)
* [Resolución 1257 de 2021 - anexos](https://www.minambiente.gov.co/wp-content/uploads/2021/12/Resolucion-1257-de-2021-Anexos.pdf)

**Listado de gestores de RCD**

* [Area Metropolitana del Valle de Aburra - AMVA](https://www.metropol.gov.co/ambiental/residuos-solidos/Paginas/RCD.aspx)
* [CORANTIOQUIA](https://www.corantioquia.gov.co/wp-content/uploads/2024/07/LISTADO-DE-GESTORES-DE-RCD-version-3-07-2024.pdf)
* [CORNARE](https://www.cornare.gov.co/residuos/rcd/Gestores_RCD_Agosto_2024.pdf)
* [CORPOURABA]()

**Colombia en mapas**

* [Municipios](https://www.colombiaenmapas.gov.co/)

**Datos**

* [Listado de gestores de RCD](./DATA/GestoresRCD.csv)
* [Ejecuciones en obra](./DATA/Items.csv)
* [Servicio de gas](./DATA/subregiones.csv)

> [!IMPORTANT]
>
> Practica EPM - Proyecto Talento Tech

## Config Virtual Environment

Crear la carpeta con el entorno virtual en el que se está trabajando

```bash
python -m venv env
```

Activar el entorno virtual desde el esquema de carpetas

```bash
env/scripts/activate
```

Crear el entorno virtual desde el archivo *.yml* con **pip**

```bash
pip install -r environment.yml
```

Crea el entorno virtual desde el archivo *.yml* con **conda**

```bash
conda env create -f environment.yml
```

Abrir Anaconda navigator

```bash
anaconda-navigator
```

Abrir en un notebook de **Jupyter**

```bash
jupyter-notebook
```

Abrir el editor de **JupyterLab**

```bash
jupyter lab
```

Crear el Dashboard a partir de notebook con **Voila**

```bash
voila notebook.ipynb
```

