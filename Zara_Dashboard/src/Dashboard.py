import streamlit as st
import pandas as pd
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Zara Sales Dashboard", layout="wide")

# Some helper funstions
@st.cache_data
def load_data():
    data = pd.read_csv("Zara_Dashboard/src/Zara_sales_dataset_preprocessed.v1.csv")
    data['DATE'] = pd.to_datetime(data['DATE'])
    data['NET_SUBSCRIBERS'] = data['SUBSCRIBERS_GAINED'] - data['SUBSCRIBERS_LOST']
    return data

df = pd.read_csv("Zara_Dashboard/src/Zara_sales_dataset_preprocessed.v1.csv")

# sidebar
st.sidebar.header('Zara Dashboard')

# countries filter
st.sidebar.header("Global Filters")
all_countries = sorted(df['Origin'].unique().tolist())
selected_countries = st.sidebar.multiselect(
    "Select Countries of Origin", 
    options=all_countries, 
    default=all_countries
)

if not selected_countries:
    selected_countries = all_countries
    st.sidebar.info("Showing all countries by default.")

filtered_df = df[df['Origin'].isin(selected_countries)]


st.sidebar.markdown('''
---
''')

# Matrics
# average revenue
avg_rev = filtered_df['revenue'].mean()
total_sold = filtered_df['Sales Volume'].sum()

# season with highest activity
seasonal_revenue = filtered_df.groupby('Season')['revenue'].sum()
best_season = seasonal_revenue.idxmax()

# most sold term
top_term = filtered_df['Terms'].mode()[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Revenue", f"${avg_rev/1e3:.1f}K")
col2.metric("Total Units Sold", f"{total_sold:,}")
col3.metric("Top Category", top_term.title())
col4.metric("Best Season", best_season)

st.divider()

# Distribution analysis
st.subheader("Distributions Analysis")
col_dist1, col_dist2 = st.columns(2)

chart_size = (5, 4)
with col_dist1:
    st.write("Price Distribution")
    
    fig1, ax1 = plt.subplots(figsize=chart_size)
    sns.kdeplot(data=filtered_df, x='Price', fill=True, color='#3498db', ax=ax1)
    
    fig1.patch.set_alpha(0)
    ax1.set_facecolor((0, 0, 0, 0)) 
    
    st.pyplot(fig1)

with col_dist2:
    st.write("Revenue Distribution")
    fig2, ax2 = plt.subplots(figsize=chart_size)
    sns.kdeplot(data=filtered_df, x='revenue', fill=True, color='#e74c3c', ax=ax2)
    
    fig2.patch.set_alpha(0)
    ax2.set_facecolor((0, 0, 0, 0))
    
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{x/1e6:.1f}M"))
    
    st.pyplot(fig2)


st.divider()
