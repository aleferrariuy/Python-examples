import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Datos
datos = [6, 8, 9, 10, 12]

# Crear figura con dos filas
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    subplot_titles=("Boxplot", "Histograma"))

# Boxplot (fila 1)
fig.add_trace(go.Box(x=datos, name="",
                     boxpoints="outliers", marker_color='skyblue'), row=1, col=1)

# Histograma (fila 2)
fig.add_trace(go.Histogram(x=datos, marker_color='lightblue', nbinsx=6), row=2, col=1)

# Layout
fig.update_layout(height=500, width=700,
                  title_text="Distribución de datos: boxplot + histograma",
                  showlegend=False)

fig.show()
