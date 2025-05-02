import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
df_review = pd.read_csv("C:/Users/Pessoal/Faculdade/Asimov/database/customer reviews.csv")
df_top100 = pd.read_csv("C:/Users/Pessoal/Faculdade/Asimov/database/Top-100 Trending Books.csv")

books = df_top100["book title"].unique()

book = st.sidebar.selectbox("Books",books)

df_book = df_top100[df_top100["book title"] == book]
df_review_f = df_review[df_review["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_year = df_book["year of publication"].iloc[0]
book_rating = df_book["rating"].iloc[0]
st.title(book_title)
st.subheader(book_genre)

col1,col2,col3 = st.columns(3)
col2.metric("Price",book_price)
col1.metric("Rating",book_rating)
col3.metric("Year of Publication",book_year)

st.divider()

for row in df_review_f.values:
    message = st.chat_message(f"{row[2]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
