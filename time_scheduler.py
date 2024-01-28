import pandas as pd
import streamlit as st
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import plotly.express as px 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from io import BytesIO
import requests
from scripts.upload_file_to_github import upload_pptx_to_github, upload_pdf_to_github
import time
import schedule
import telebot
from spire.presentation import Presentation as Presentation2, FileFormat
from styles.styles import body_css

body_css()

#read aggregated data
donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"
df = pd.read_csv(donations_state_url)
df.date = pd.to_datetime(df.date).dt.date
df['year'] = df['date'].astype('str').apply(lambda x: x[:4])
max_date = max(df.date)

column = st.columns([7,2])
column[0].write("""### Status of Data""")
column[1].write(""" """)
column[1].write(""" Data as of {}""".format(max_date))

df = df[df.year == '2024']

negeri_total_value = [df[(df.state == "{}".format(x))].daily.sum() for x in sorted(df.state.unique())]
[johor_total, kedah_total, kelantan_total, malaysia_total, melaka_total, negeri_sembilan_total, 
pahang_total, perak_total, pulau_pinang_total, sabah_total, sarawak_total, selangor_total, 
terengganu_total, kuala_lumpur_total] = negeri_total_value

negeri_value = [df[(df.date == df.date.max()) & (df.state == "{}".format(x))].daily.iloc[0] for x in sorted(df.state.unique())]
[johor, kedah, kelantan, malaysia, melaka, negeri_sembilan, 
pahang, perak, pulau_pinang, sabah, sarawak, selangor, 
terengganu, kuala_lumpur] = negeri_value

url_to_check = 'https://github.com/hazimutalib/blood_donation/blob/main/infographic/blood_donation_{}.pdf'.format(max_date)
response = requests.get(url_to_check)

def job():
    st.write(datetime.now())
    today_date = datetime.now().date()
    difference = today_date - max_date
    if (difference.days == 1) & (response.status_code // 100 != 2):
        repo_owner = 'hazimutalib'
        repo_name = 'blood_donation'
        template_path = './blood_donation.pptx'
        file_path = './infographic/blood_donation_{}.pptx'.format(max(df.date))
        lol = 'ghp_XQuAk8BlOgV2PNLwq3qWbuMG0DwuQI46YKk0'

        lol = lol.replace('2','1').replace('3','2').replace('4','3').replace('6','5')


        upload_pptx_to_github(repo_owner, repo_name, template_path, file_path, lol, malaysia_total, kuala_lumpur_total, kedah_total, 
                            perak_total, johor_total, sarawak_total, pulau_pinang_total, sabah_total, melaka_total, selangor_total, 
                            negeri_sembilan_total, terengganu_total, pahang_total, kelantan_total, max_date, malaysia, kuala_lumpur, kedah, 
                            perak, johor, sarawak, pulau_pinang, sabah, melaka, selangor, 
                            negeri_sembilan, terengganu, pahang, kelantan)

        file_path_pdf = './infographic/blood_donation_{}.pdf'.format(max_date)
        presentation2 = Presentation2()
        presentation2.LoadFromFile(file_path)
        presentation2.SaveToFile(file_path_pdf, FileFormat.PDF)
        presentation2.Dispose()
        upload_pdf_to_github(file_path_pdf, lol, repo_owner, repo_name)

        tkn = '6430193325:AAFkiOTYhb574_owPQVunkNHslzIxRAtNX8'

        bot = telebot.TeleBot(tkn)

        channel_id = '@blood_donatio'
        message = """
        🩸 **Blood Donation Update of 2024 - Data as of {}** 🩸
        📈 Today's Blood Donation Count:
        - Total Donations: {:,}
        - Latest Daily Donations: {:,}

        Thank you to all donors for making a difference! 💖
        #BloodDonation #DonateLife #SaveLives

                        """.format(max_date, malaysia_total, malaysia)
        try:
            bot.send_message(channel_id, message, parse_mode='Markdown')
            with open(file_path_pdf, 'rb') as file:
                bot.send_document(channel_id, file)
        except:
            print('Message failed to send')

        x = 0

    else:
        st. write('###### Data has not been updated')


schedule.every(60).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1800)