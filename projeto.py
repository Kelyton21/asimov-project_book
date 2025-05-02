import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df_review = pd.read_csv("C:/Users/Pessoal/Faculdade/Asimov/database/customer reviews.csv")
df_top100 = pd.read_csv("C:/Users/Pessoal/Faculdade/Asimov/database/Top-100 Trending Books.csv")

max_price_book = df_top100["book price"].max()
min_price_book = df_top100["book price"].min()
price = st.sidebar.slider("Faixa de Preço",min_price_book,max_price_book,min_price_book)

#df_top100[df_top100["book title"].str.contains(("Harry Potter"))]
#df_top100[df_top100["book price"]
df_book = df_top100[df_top100["book price"] >= price]

df_book
# Fazendo um grafico de barras
fig = px.bar(df_book["year of publication"].value_counts())
# Fazendo um histograma
fig2 = px.histogram(df_book["book price"])

col1,col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)