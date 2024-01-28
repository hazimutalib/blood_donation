import pandas as pd
import streamlit as st
from styles.styles import kpi_box_css, body_css,  plotly_css
from scripts.components import yesterday_trends, historical_trends, retention_trends


#set the layout of the web app 
st.set_page_config(layout="centered")


#css style
body_css()
plotly_css()
kpi_box_css()


import time
import schedule
import telebot

API_TOKEN = '6430193325:AAFkiOTYhb574_owPQVunkNHslzIxRAtNX8'
bot = telebot.TeleBot(API_TOKEN)

channel_id = '@blood_donatio'


def job():
    print("Job is running...")
    try:
        bot.send_message(channel_id, 'Hello, World!')
        file_path = '.infographics/blood_donation.pdf'

    except:
        print('Message failed to send')


schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)



#read aggregated data
donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"
df = pd.read_csv(donations_state_url)
df.date = pd.to_datetime(df.date).dt.date
df['year'] = df['date'].astype('str').apply(lambda x: x[:4])


#web app tabs
tab1, tab2, tab3 = st.tabs(["Latest daily trends", "Historical trends", "Blood retention trends"])
with tab1:
   yesterday_trends(df)

with tab2:
   historical_trends(df)

with tab3:
   retention_trends()



