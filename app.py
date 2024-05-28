import pandas as pd
import plotly.express as px
import streamlit as st
import random

st.set_page_config(page_title = "Spotify Dashboard",
                   page_icon=":barchart:",
                   layout = "wide")

def load_data():
    try:
        df = pd.read_csv("./spotify_songs.csv", encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv("./spotify_songs.csv", encoding='latin1')
        except UnicodeDecodeError:
            df = pd.read_csv("./spotify_songs.csv", encoding='iso-8859-1')
    df.columns = df.columns.str.replace('_', '')
    return df 

df = load_data()

st.sidebar.header("Please Filter Here:")

artist = st.sidebar.multiselect(
    "Select the Artist:",
    options = df["artist(s)name"].unique()
)

releaseyear = st.sidebar.multiselect(
    "Select the Release Year:",
    options = df["releasedyear"].unique()
)
query = "`artist(s)name` == @artist"
if releaseyear:
    query += f" & `releasedyear` == {releaseyear}"

df_selection = df.query(query)
st.dataframe(df_selection)