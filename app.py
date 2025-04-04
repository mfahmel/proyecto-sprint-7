import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de anuncios de coches')

if st.button('Mostrar histograma'):
    st.write('Histograma de odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.button('Mostrar gráfico de dispersión'):
    st.write('Dispersión entre precio y año del modelo')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
