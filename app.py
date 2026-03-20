import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Dados de anúncios de vendas de carros')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # Criar botão
disp_button = st.button('Criar gráfico de Dispersão') 

if hist_button: # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros') # escreve uma mensagem
    fig = px.histogram(car_data, x="odometer") # cria um histograma
    st.plotly_chart(fig, use_container_width=True) # exibe um gráfico Plotly interativo

if disp_button:
    st.write('Criando um gráfico de Dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)  