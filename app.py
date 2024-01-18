import pandas as pd
import streamlit as st

donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"

df = pd.read_csv(donations_state_url)
df.to_csv('test.csv')
st.write(df)

