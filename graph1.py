import pandas as pd
import plotly.graph_objects as go # Importación de plotly.graph_objects como go

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un histograma utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de histograma
fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

# Opcional: Puedes añadir un título al gráfico si lo deseas
fig.update_layout(title_text='Distribución del Odómetro')

# Mostrar el gráfico Plotly
fig.show()