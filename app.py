import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests
import os
import subprocess
from io import BytesIO


books = pickle.load(open("books.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))



def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x:x[1], reverse=True)[1:6]

    recs = []
    for i in similar_items:
        b_title = pt.index[i[0]]
        cover_series = books.loc[books['Book-Title'] == pt.index[i[0]]]['Image-URL-M']
        if len(cover_series) > 0 and isinstance(cover_series.iloc[0], str) and cover_series.iloc[0].strip() != "":
            b_cover = cover_series.iloc[0]
        else:
            b_cover = "https://via.placeholder.com/150x220?text=No+Cover"
        recs.append((b_title, b_cover))

    return recs




st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("Book Recommendation System")

selected_book_name = st.selectbox(
    "Choose a Book:",
    sorted(books['Book-Title'].drop_duplicates().values)
)

if st.button("Recommend"):
    st.write(f"You selected: {selected_book_name}")
    recs = recommend(selected_book_name)
    st.write("Recommendations: ")
    # for rec in recs:
    #     st.write(rec)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recs[0][0])
        st.image(recs[0][1])
    with col2:
        st.text(recs[1][0])
        st.image(recs[1][1])
    with col3:
        st.text(recs[2][0])
        st.image(recs[2][1])
    with col4:
        st.text(recs[3][0])
        st.image(recs[3][1])
    with col5:
        st.text(recs[4][0])
        st.image(recs[4][1])





st.write("Developed by Manish Harsha Bajracharya")