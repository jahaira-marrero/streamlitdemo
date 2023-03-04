import streamlit as st 
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt
import requests


st.header('SAFEST NYC AREAS')

data = requests.get("https://data.cityofnewyork.us/resource/qgea-i56i.json").json()
@st.cache_data
def load_data(url):
    df = pd.read_json(data)
    return df

df = load_data("https://data.cityofnewyork.us/resource/qgea-i56i.json")
st.dataframe(df)

st.button("Rerun")

