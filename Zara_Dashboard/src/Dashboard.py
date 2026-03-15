import streamlit as st
import pandas as pd
from datetime import timedelta, datetime

# Set page config
st.set_page_config(page_title="Zara Sales Dashboard", layout="wide")

# Some helper funstions
@st.cache_data
def load_data():
    data = pd.read_csv("Zara_Dashboard/src/Zara_sales_dataset_preprocessed.csv")
    data['DATE'] = pd.to_datetime(data['DATE'])
    data['NET_SUBSCRIBERS'] = data['SUBSCRIBERS_GAINED'] - data['SUBSCRIBERS_LOST']
    return data

df = pd.read_csv("Zara_Dashboard/src/Zara_sales_dataset_preprocessed.csv")

# sidebar
st.sidebar.header('Zara Dashboard')

# countries filter
countries = ['All'] + sorted(df['Origin'].unique().tolist())

selected_country = st.sidebar.selectbox("Select Country of Origin", countries)
if selected_country != 'All':
    filtered_df = df[df['Origin'] == selected_country]
else:
    filtered_df = df


st.sidebar.markdown('''
---
''')
