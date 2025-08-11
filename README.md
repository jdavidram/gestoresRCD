<table border=1 border-collapse="collapse" width="100%">
  <thead>
    <th>
      <img src="https://static.wikia.nocookie.net/logopedia/images/5/52/EPM2007.png/revision/latest?cb=20210505181105&path-prefix=es" width="320px" height="270px" />
    </th>
    <th>
      <h1>Gestores de RCD</h1>
    </th>
  </thead>
</table>

> [!NOTE]
> Practica EPM - Proyecto Talento Tech
> 
> Tomas esta implementado el mapa en python
> 
> Darwin esta buscando un modelo predictivo adeacuado al proyecto
> 
> David hara el relacionamiento de tablas
> 
> Bilmar adelantara el texto en el github

## Análisis Espacial para la Gestión de Residuos de Construcción y Demolición (RCD) en Antioquia
    esta sujeto a cambios
    
## Introducción

La gestión adecuada de los residuos de construcción y demolición (RCD) es un componente esencial para el desarrollo sostenible en el sector de la construcción. En Colombia, y particularmente en el departamento de Antioquia, el crecimiento urbano ha generado un aumento significativo en la generación de RCD, lo que plantea retos importantes en términos de aprovechamiento y disposición final. Este trabajo propone una metodología de análisis espacial que permite vincular las ejecuciones de obra con los gestores de RCD autorizados en la región. Para ello, se emplearon diagramas de Voronoi como herramienta para delimitar las áreas de cobertura de cada gestor, facilitando la identificación de las obras que potencialmente pudieron haber gestionado sus residuos de manera más eficiente. Esta aproximación busca contribuir al fortalecimiento de la planificación ambiental territorial y a la optimización de los sistemas de gestión de RCD en Antioquia.

A continuación, presento una tabla con el ancho de las canalizaciones hechas (0.25 metros) y las profundidades en metros de cada una de las diferentes capas en cada una de las canalizaciones.

<table border-collapse="collapse">
    <thead>
        <tr>
            <th rowspan="2" colspan="2" style="text-align: center;">Canalizacion</th>
            <th colspan="4" style="text-align: center;">RCD</th>
        </tr>
        <tr>
            <th style="text-align: center;">Tierras</th>
            <th style="text-align: center;">Base</th>
            <th style="text-align: center;">Concreto</th>
            <th style="text-align: center;">PvF</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Canalizacion tuberia en zona verde</td>
            <td>0.25</td>
            <td>0.60</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Canalizacion tuberia en anden</td>
            <td>0.25</td>
            <td>0.30</td>
            <td>0.20</td>
            <td>0.10</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Canalizacion tuberia en cuneta</td>
            <td>0.25</td>
            <td>0.40</td>
            <td>0.20</td>
            <td>0.10</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Canalizacion tuberia en asfalto</td>
            <td>0.25</td>
            <td>0.30</td>
            <td>0.30</td>
            <td>0</td>
            <td>0.10</td>
        </tr>
        <tr>
            <td>Canalizacion tuberia en concreto</td>
            <td>0.25</td>
            <td>0.30</td>
            <td>0.20</td>
            <td>0.20</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Canalizacion tuberia en adoquin</td>
            <td>0.25</td>
            <td>0.40</td>
            <td>0.20</td>
            <td>0.10</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Canalizacion tuberia en destapado</td>
            <td>0.25</td>
            <td>0.30</td>
            <td>0.40</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </tbody>
</table>

## Objetivo general 
Desarrollar un análisis espacial integral de la gestión de Residuos de Construcción y Demolición (RCD) en Antioquia, que permita cuantificar el potencial de aprovechamiento de materiales no gestionados adecuadamente y generar predicciones de demanda futura, con el fin de optimizar la planificación territorial y fortalecer los sistemas de gestión sostenible de RCD en el departamento.

## Resumen ejecutivo
El presente proyecto aborda uno de los desafíos ambientales y logísticos más significativos que enfrenta el sector de la construcción la ciudad de Medellín: la gestión ineficiente de los Residuos de Construcción y Demolición (RCD). En el contexto del acelerado crecimiento urbano y la expansión de infraestructura en la ciudad, se ha identificado una desconexión crítica entre los generadores de estos residuos (principalmente empresas constructoras) y los gestores autorizados para su manejo, lo que deriva en múltiples problemáticas ambientales, económicas y operativas.
La situación actual se caracteriza por una marcada asimetría en la distribución espacial de la capacidad instalada para el manejo de RCD y los puntos de generación de estos residuos. Por un lado, numerosas obras de construcción desarrollan sus actividades sin acceso a información clara sobre los gestores autorizados más cercanos, mientras que, por otro lado, muchos centros de aprovechamiento operan por debajo de su capacidad máxima debido a esta falta de vinculación estratégica. Esta desconexión genera costos logísticos innecesarios, subutilización de la infraestructura disponible y, en última instancia, conduce a prácticas inadecuadas de disposición final.
El proyecto propone implementar una metodología innovadora basada en análisis espacial avanzado, específicamente mediante el uso de diagramas de Voronoi, para establecer un sistema de asignación territorial que optimice la gestión de RCD. Esta aproximación permitirá delimitar áreas de cobertura lógica para cada gestor autorizado, considerando no solo la proximidad geográfica sino también variables como capacidad de procesamiento, tipos de materiales aceptados y condiciones de acceso.
La importancia de esta iniciativa trasciende el ámbito operativo inmediato, ya que sus resultados contribuirán directamente a tres dimensiones fundamentales:
Dimensión ambiental: Al facilitar el flujo adecuado de RCD hacia los gestores autorizados, se reducirá significativamente la disposición inadecuada en botaderos ilegales, disminuyendo así el impacto negativo sobre suelos, fuentes hídricas y paisajes urbanos.
Dimensión económica: La optimización de las rutas de recolección y transporte generará ahorros sustanciales para las empresas constructoras, mientras que los gestores podrán operar con mayor eficiencia al incrementar su volumen de procesamiento.
Dimensión regulatoria: Los hallazgos del proyecto proporcionarán insumos valiosos para el diseño de políticas públicas más efectivas en materia de gestión de RCD, permitiendo a las autoridades ambientales tomar decisiones basadas en evidencia espacial concreta

## Stakeholders Clave
Los principales actores identificados son:
**Constructores:** Tienen dificultades para localizar gestores autorizados cercanos y enfrentan altos costos de disposición.
**Gestores de RCD:** Subutilizan su capacidad instalada debido a la falta de vinculación efectiva con las obras.
**Autoridades ambientales:** Carecen de datos precisos para fiscalizar y planificar infraestructura de gestión de RCD.
**Comunidad:** Sufre los efectos de la contaminación y los riesgos asociados a los botaderos ilegales.

## "¿Cómo podríamos ayudar a los constructores de Antioquia a identificar y seleccionar gestores autorizados de RCD cercanos a sus obras, para reducir costos logísticos y aumentar el aprovechamiento de materiales?"

## Bibliografia

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

## Config Virtual Environment

Crea el entorno virtual desde el archivo **.yml**:

```bash
conda env create -f environment.yml
```
