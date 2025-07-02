import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Simulación de datos de presión arterial sistólica
np.random.seed(42)
presion_sistolica = np.random.normal(loc=125, scale=10, size=100)
presion_sistolica = np.round(presion_sistolica, 1)

# Crear figura con dos filas
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    subplot_titles=("Boxplot de Presión Sistólica", "Histograma de Presión Sistólica"))

# Boxplot (fila 1)
fig.add_trace(go.Box(x=presion_sistolica, name="Presión", marker_color='lightcoral',
                     boxpoints="outliers"), row=1, col=1)

# Histograma (fila 2)
fig.add_trace(go.Histogram(x=presion_sistolica, nbinsx=15, marker_color='salmon'), row=2, col=1)

# Layout general
fig.update_layout(height=600, width=800,
                  title_text="Distribución de la Presión Arterial Sistólica en Pacientes",
                  xaxis_title="mmHg", showlegend=False)

fig.show()
