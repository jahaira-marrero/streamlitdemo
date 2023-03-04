import streamlit as st 
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt
import requests


st.header('SAFEST NYC AREAS')

data = requests.get("https://data.cityofnewyork.us/resource/qgea-i56i.json").json()
@st._experimental_singleton
st.json(data, expanded=True)

