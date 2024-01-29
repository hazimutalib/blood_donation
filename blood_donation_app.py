import pandas as pd
import streamlit as st
from styles.styles import kpi_box_css, body_css,  plotly_css
from scripts.components import latest_trends, historical_trends, retention_trends


#set the layout of the web app 
st.set_page_config(layout="centered")

#css style
body_css()
plotly_css()
kpi_box_css()


#read aggregated data
donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"
df = pd.read_csv(donations_state_url)
df.date = pd.to_datetime(df.date).dt.date
df['year'] = df['date'].astype('str').apply(lambda x: x[:4])
max_date = max(df.date)


#web app tabs
tab1, tab2, tab3 = st.tabs(["Latest daily trends", "Historical trends", "Blood retention trends"])
with tab1:
   latest_trends(df, max_date)

with tab2:
   historical_trends(df)

with tab3:
   retention_trends()
