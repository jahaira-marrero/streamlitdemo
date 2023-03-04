import streamlit as st 
import pandas as pd
from sodapy import Socrata
import numpy as np
import pydeck as pdk
import altair as alt
import requests


st.header('SAFEST NYC AREAS')

data = requests.get("https://data.cityofnewyork.us/resource/qgea-i56i.json").json()
client = Socrata("data.cityofnewyork.us", None)

@st.cache_data
def load_data(url):
    results = client.get()
    results_df = pd.DataFrame.from_records(results)
    return results_df


