import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Iniciar la app
app = dash.Dash(__name__)
app.title = "Proyecto de Análisis de Datos"

# Simulamos un DataFrame de ejemplo para gráficas
df = pd.DataFrame({
    'Año': [2021, 2021, 2022, 2022, 2023, 2023],
    'Categoría': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Valor': [100, 150, 120, 180, 130, 200]
})

# Layout
app.layout = html.Div([
    
    # 🎯 Banner principal
    html.Div([
        html.H1(
            "Análisis de Datos para la Gestión de Residuos de Construcción y Demolición (RCD) en Antioquia",
            style={'textAlign': 'center', 'color': 'white'}
        ),
    ], style={'backgroundColor': "#97D700", 'padding': '20px'}),

    # 📁 Pestañas
    dcc.Tabs([
        # 📄 TAB 1: Contexto
        dcc.Tab(label='Contexto del Proyecto', children=[
            html.Div([
                html.H2("Introducción", style={'color': '#2E7D32'}),
                html.P(
                    "La gestión de Residuos de Construcción y Demolición (RCD) es un reto creciente en Antioquia, "
                    "impulsado por el acelerado crecimiento urbano. A pesar de la existencia de gestores autorizados "
                    "para su aprovechamiento, muchas obras no logran vincularse eficientemente con ellos, lo que genera "
                    "impactos ambientales, económicos y logísticos."
                ),

                html.H2("Objetivo General", style={'color': '#2E7D32'}),
                html.P(
                    "Optimizar la asignación de obras a gestores autorizados de RCD mediante análisis de datos, reduciendo impactos ambientales, costos logísticos y mejorando la planificación territorial."
                ),

                html.H2("Problema Abordado", style={'color': '#2E7D32'}),
                html.P(
                    "La desconexión entre obras y gestores autorizados provoca disposición inadecuada de RCD, "
                    "desaprovechaminento de materiales generados y altos costos de transporte."
                ),
                html.Img(
                    src="/assets/escombros.png",
                    style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginRight': '2%'}
                ),
                html.Img(
                    src="/assets/escombrera.png",
                    style={'width': '34%', 'display': 'inline-block', 'verticalAlign': 'top'}
                ),
                html.H2("Impacto Esperado", style={'color': '#2E7D32'}),
                html.Ul([
                    html.Li("🌱 Ambiental: Mejorar la eficiencia en la gestión de los residuos."),
                    html.Li("💰 Económico: Disminución de costos logísticos y mayor eficiencia operativa."),
                    html.Li("📊 Regulatorio: Datos precisos para fortalecer políticas públicas.")
                ]),
            ], style={'padding': '20px', 'lineHeight': '1.6', 'fontSize': '16px'})
        ]),

        # 📊 TAB 2: Análisis Descriptivo
        dcc.Tab(label='Análisis Descriptivo', children=[
            html.Div([
                html.H2("Gráficos Descriptivos"),

                html.P("Aquí puedes incluir gráficos de evolución, histogramas, boxplots, etc."),

                # Ejemplo: gráfico de línea
                dcc.Graph(
                    figure=px.line(df[df['Categoría'] == 'A'], x='Año', y='Valor', title='Evolución Categoría A')
                ),

                # Segundo gráfico
                dcc.Graph(
                    figure=px.bar(df, x='Año', y='Valor', color='Categoría', barmode='group',
                                  title='Comparación de categorías por año')
                ),
            ], style={'padding': '20px'})
        ]),

        # 🧠 TAB 3: Análisis Predictivo
        dcc.Tab(label='Análisis Predictivo', children=[
            html.Div([
                html.H2("Predicciones y Mapas"),
                html.P("Aquí puedes insertar mapas interactivos y tus modelos predictivos."),

                # Mapa simple (usando datos de ejemplo de px)
                dcc.Graph(
                    figure=px.scatter_map(
                        px.data.carshare(),  # dataset de ejemplo
                        lat="centroid_lat", lon="centroid_lon", size="car_hours",
                        color="peak_hour", zoom=10,
                        map_style="open-street-map",
                        title="Ejemplo de Mapa Interactivo"
                    )
                ),

                # Placeholder para predicción
                html.Div([
                    html.H4("Modelo Predictivo:"),
                    html.P("Aquí podrías mostrar resultados de regresión, clasificación o predicciones generadas."),
                    html.P("Ejemplo: predicción de ventas para el próximo año.")
                ])
            ], style={'padding': '20px'})
        ])
    ])
])

if __name__ == "__main__":
    app.run(debug=True)
