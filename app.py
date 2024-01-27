import pandas as pd
import streamlit as st
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import plotly.express as px 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from io import BytesIO
import requests
from styles.styles import kpi_box_malaysia, kpi_box_css, body_css, kpi_box_granular
from styles.styles import kpi_box_kuala_lumpur, kpi_box_kedah, kpi_box_perak, kpi_box_johor, kpi_box_sarawak, kpi_box_pulau_pinang, kpi_box_sabah, kpi_box_melaka
from styles.styles import kpi_box_selangor, kpi_box_negeri_sembilan, kpi_box_terengganu, kpi_box_pahang, kpi_box_kelantan, kpi_box_perlis, kpi_box_putrajaya, kpi_box_labuan
from scripts.upload_pptx_to_github import upload_pptx_to_github, upload_pdf_to_github
import time
import telebot
from spire.presentation import Presentation as Presentation2, FileFormat


st.set_page_config(layout="centered")



body_css()

st.markdown(
    f"""
    <style>
    .stPlotlyChart {{
     outline: 10px solid {'#FFFFFF'};
     border-radius: 8px;
     box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.20), 0 6px 20px 0 rgba(0, 0, 0, 0.30);
    }}
    </style>
    """, unsafe_allow_html=True
)


donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"
kpi_box_css()
df = pd.read_csv(donations_state_url)
df.date = pd.to_datetime(df.date).dt.date
df['year'] = df['date'].astype('str').apply(lambda x: x[:4])



def historical_trends(df):
    df = df[df.year != '2024']

    column = st.columns([7,2])
    column[0].write("""### Malaysia's Blood Donation Yearly Trends (2006 - 2023)""")
    column[1].write("""  """)
    column[1].write("""  Data as of {}""".format(max(df.date)))


    malaysia_sum = df[df.state == 'Malaysia'].daily.sum()

    kpi_box_malaysia(malaysia_sum)



    fig = px.line(df[df.state == 'Malaysia'].groupby(['year','state'])['daily'].sum().reset_index(), x = 'year', y = 'daily',
                 height = 540, title = 'Time series of blood donors by year across Malaysia (2006 - 2023)')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    st.write(fig)

    st.write("""# """)

    fig = px.bar(df[df.state != 'Malaysia'].groupby('state')['daily'].sum(), orientation='h', text_auto='.2s',  height = 540, 
                title = 'Cumulative count of blood donors by state (2006 - 2023)',)
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_xaxes(showticklabels=False)
    st.write(fig)
    
    st.write("""# """)


    fig = px.line(df[(df.state != 'Malaysia')].groupby(['year','state'])['daily'].sum().reset_index(), x = 'year', y = 'daily', color = 'state',
                 height = 540, title = 'Time series of blood donors across state of Malaysia (2006 - 2023)')
    # fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    st.write(fig)



def yesterday_trends(df):
    column = st.columns([7,2])
    column[0].write("""### Malaysia's Blood Donation Daily Updates (2024)""")
    column[1].write(""" """)
    column[1].write(""" Data as of {}""".format(max(df.date)))

    df = df[df.year == '2024']
    malaysia = df[(df.date == df.date.max()) & (df.state == "Malaysia")].daily
    kedah = df[(df.date == df.date.max()) & (df.state == "Kedah")].daily
    pulau_pinang = df[(df.date == df.date.max()) & (df.state == "Pulau Pinang")].daily
    perak = df[(df.date == df.date.max()) & (df.state == "Perak")].daily
    selangor = df[(df.date == df.date.max()) & (df.state == "Selangor")].daily
    kuala_lumpur = df[(df.date == df.date.max()) & (df.state == "W.P. Kuala Lumpur")].daily
    negeri_sembilan = df[(df.date == df.date.max()) & (df.state == "Negeri Sembilan")].daily
    sabah = df[(df.date == df.date.max()) & (df.state == "Sabah")].daily
    sarawak = df[(df.date == df.date.max()) & (df.state == "Sarawak")].daily
    kelantan = df[(df.date == df.date.max()) & (df.state == "Kelantan")].daily
    terengganu= df[(df.date == df.date.max()) & (df.state == "Terengganu")].daily
    pahang = df[(df.date == df.date.max()) & (df.state == "Pahang")].daily
    melaka = df[(df.date == df.date.max()) & (df.state == "Melaka")].daily
    johor = df[(df.date == df.date.max()) & (df.state == "Johor")].daily

    malaysia_total = df[(df.state == "Malaysia")].daily.sum()
    kedah_total = df[(df.state == "Kedah")].daily.sum()
    pulau_pinang_total = df[(df.state == "Pulau Pinang")].daily.sum()
    perak_total = df[(df.state == "Perak")].daily.sum()
    selangor_total = df[(df.state == "Selangor")].daily.sum()
    kuala_lumpur_total = df[(df.state == "W.P. Kuala Lumpur")].daily.sum()
    negeri_sembilan_total = df[(df.state == "Negeri Sembilan")].daily.sum()
    sabah_total = df[(df.state == "Sabah")].daily.sum()
    sarawak_total = df[(df.state == "Sarawak")].daily.sum()
    kelantan_total = df[(df.state == "Kelantan")].daily.sum()
    terengganu_total= df[(df.state == "Terengganu")].daily.sum()
    pahang_total = df[(df.state == "Pahang")].daily.sum()
    melaka_total = df[(df.state == "Melaka")].daily.sum()
    johor_total = df[(df.state == "Johor")].daily.sum()

    

    
    tab1, tab2 = st.tabs(["Cumulative count of blood donations", "Yesterday count of blood donations"])

    with tab1:

        kpi_box_malaysia(malaysia_total)
        column = st.columns([1,1,1,1])
        column[0].markdown(kpi_box_kuala_lumpur(kuala_lumpur_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_kedah(kedah_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_perak(perak_total), unsafe_allow_html=True )
        column[3].markdown(kpi_box_johor(johor_total), unsafe_allow_html=True )

        column[0].markdown(kpi_box_sarawak(sarawak_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_pulau_pinang(pulau_pinang_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_sabah(sabah_total), unsafe_allow_html=True )
        column[3].markdown(kpi_box_melaka(melaka_total), unsafe_allow_html=True )

        column[0].markdown(kpi_box_selangor(selangor_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_negeri_sembilan(negeri_sembilan_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_terengganu(terengganu_total), unsafe_allow_html=True )
        column[3].markdown(kpi_box_pahang(pahang_total), unsafe_allow_html=True )

        column[0].markdown(kpi_box_kelantan(kelantan_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_perlis(0), unsafe_allow_html=True )
        column[2].markdown(kpi_box_putrajaya(0), unsafe_allow_html=True )
        column[3].markdown(kpi_box_labuan(0), unsafe_allow_html=True )


    with tab2:
        kpi_box_malaysia(malaysia.iloc[0])
        column = st.columns([1,1,1,1])
        column[0].markdown(kpi_box_kuala_lumpur(kuala_lumpur.iloc[0]), unsafe_allow_html=True )
        column[1].markdown(kpi_box_kedah(kedah.iloc[0]), unsafe_allow_html=True )
        column[2].markdown(kpi_box_perak(perak.iloc[0]), unsafe_allow_html=True )
        column[3].markdown(kpi_box_johor(johor.iloc[0]), unsafe_allow_html=True )

        column[0].markdown(kpi_box_sarawak(sarawak.iloc[0]), unsafe_allow_html=True )
        column[1].markdown(kpi_box_pulau_pinang(pulau_pinang.iloc[0]), unsafe_allow_html=True )
        column[2].markdown(kpi_box_sabah(sabah.iloc[0]), unsafe_allow_html=True )
        column[3].markdown(kpi_box_melaka(melaka.iloc[0]), unsafe_allow_html=True )

        column[0].markdown(kpi_box_selangor(selangor.iloc[0]), unsafe_allow_html=True )
        column[1].markdown(kpi_box_negeri_sembilan(negeri_sembilan.iloc[0]), unsafe_allow_html=True )
        column[2].markdown(kpi_box_terengganu(terengganu.iloc[0]), unsafe_allow_html=True )
        column[3].markdown(kpi_box_pahang(pahang.iloc[0]), unsafe_allow_html=True )

        column[0].markdown(kpi_box_kelantan(kelantan.iloc[0]), unsafe_allow_html=True )
        column[1].markdown(kpi_box_perlis(0), unsafe_allow_html=True )
        column[2].markdown(kpi_box_putrajaya(0), unsafe_allow_html=True )
        column[3].markdown(kpi_box_labuan(0), unsafe_allow_html=True )

    
    st.write("""#  """)

    fig = px.line(df[(df.state == 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', 
                   title = 'Time series of blood donors of Malaysia (YTD)')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    st.write(fig)

    st.write("""#  """)

    fig = px.line(df[(df.state != 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', color = 'state',
                  title = 'Time series of blood donors across state (YTD)')
    # fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    
    st.write(fig)

    if st.button('Upload'):
        repo_owner = 'hazimutalib'
        repo_name = 'blood_donation'
        template_path = './blood_donation.pptx'
        file_path = './infographic/blood_donation_{}.pptx'.format(max(df.date))
        lol = 'ghp_XQuAk8BlOgV2PNLwq3qWbuMG0DwuQI46YKk0'
        
        lol = lol.replace('2','1').replace('3','2').replace('4','3').replace('6','5')


        upload_pptx_to_github(repo_owner, repo_name, template_path, file_path, lol, malaysia_total, kuala_lumpur_total, kedah_total, 
                              perak_total, johor_total, sarawak_total, pulau_pinang_total, sabah_total, melaka_total, selangor_total, 
                             negeri_sembilan_total, terengganu_total, pahang_total, kelantan_total, max(df.date), malaysia.iloc[0], kuala_lumpur.iloc[0], kedah.iloc[0], 
                              perak.iloc[0], johor.iloc[0], sarawak.iloc[0], pulau_pinang.iloc[0], sabah.iloc[0], melaka.iloc[0], selangor.iloc[0], 
                             negeri_sembilan.iloc[0], terengganu.iloc[0], pahang.iloc[0], kelantan.iloc[0])
        

        file_path_pdf = './infographic/blood_donation_{}.pdf'.format(max(df.date))
        presentation2 = Presentation2()
        presentation2.LoadFromFile(file_path)
        presentation2.SaveToFile(file_path_pdf, FileFormat.PDF)
        presentation2.Dispose()
        upload_pdf_to_github(file_path_pdf, lol, repo_owner, repo_name)

        tkn = '6430193325:AAFkiOTYhb574_owPQVunkNHslzIxRAtNX8'

        bot = telebot.TeleBot(tkn)

        channel_id = '@blood_donatio'
        message = """
        🩸 **Blood Donation Update - {}** 🩸
        📈 Today's Blood Donation Count:
        - Total Donations: [Total Count]
        - New Donations: [New Count]

        Thank you to all donors for making a difference! 💖
        #BloodDonation #DonateLife #SaveLives
   
                        """.format(max(df.date))
        try:
            bot.send_message(channel_id, message, parse_mode='Markdown')
            with open(file_path_pdf, 'rb') as file:
                bot.send_document(channel_id, file)
        except:
            print('Message failed to send')






def retention_trends():
    st.write("""### Malaysia's Blood Donors Retention Trends (2012 - 2024)""")
    parquet_file_url = 'https://dub.sh/ds-data-granular'
    response = requests.get(parquet_file_url)
    parquet_data = BytesIO(response.content)
    df_granular = pq.read_pandas(parquet_data).to_pandas()
    df_granular.visit_date = pd.to_datetime(df_granular.visit_date).dt.date
    donors = len(df_granular.donor_id)
    unique_donors = len(df_granular.donor_id.unique())

    kpi_box_granular(donors, unique_donors)

    df_granular['visit_year'] = pd.to_datetime(df_granular.visit_date).dt.year
    df_granular['visit_age'] = df_granular.visit_year - df_granular.birth_date



    df_new = df_granular.groupby(['donor_id'])['birth_date'].mean().sort_values(ascending=False).reset_index()
    df_new['age'] = 2024 - df_new['birth_date']
    df_new['age_band'] = ''
    df_new.age_band[df_new.age < 18] = '0 - 17'
    df_new.age_band[(df_new.age >= 18) & (df_new.age < 30)] = '18-29'
    df_new.age_band[(df_new.age >= 30) & (df_new.age < 40)] = '30-39'
    df_new.age_band[(df_new.age >= 40) & (df_new.age < 50)] = '40-49'
    df_new.age_band[(df_new.age >= 50) & (df_new.age < 60)] = '50-59'
    df_new.age_band[(df_new.age >= 60)] = '60>='
    df_new1  = df_new.groupby(['age_band'])['age_band'].count()


    df_new2 = df_granular
    df_new2['visit_age_band'] = ''
    df_new2.visit_age_band[df_new2.visit_age < 18] = '0 - 17'
    df_new2.visit_age_band[(df_new2.visit_age >= 18) & (df_new2.visit_age < 30)] = '18-29'
    df_new2.visit_age_band[(df_new2.visit_age >= 30) & (df_new2.visit_age < 40)] = '30-39'
    df_new2.visit_age_band[(df_new2.visit_age >= 40) & (df_new2.visit_age < 50)] = '40-49'
    df_new2.visit_age_band[(df_new2.visit_age >= 50) & (df_new2.visit_age < 60)] = '50-59'
    df_new2.visit_age_band[(df_new2.visit_age >= 60)] = '60>='
    df_new3  = df_new2.groupby(['visit_age_band'])['visit_age_band'].count()
    

    df_new4 = df_granular.groupby('donor_id')['visit_date'].count().reset_index()
    df_new5 = df_new4.groupby('visit_date')['donor_id'].count().reset_index()
    df_new5['frequency'] = df_new5.visit_date.astype('str')
    df_new5.frequency[(df_new5.visit_date == 1)] = '1'
    df_new5.frequency[(df_new5.visit_date == 2)] = '2'
    df_new5.frequency[(df_new5.visit_date >= 3) & (df_new5.visit_date < 10)] = '3 - 9'
    df_new5.frequency[(df_new5.visit_date >= 10) & (df_new5.visit_date < 20)] = '10 - 19'
    df_new5.frequency[(df_new5.visit_date >= 20) & (df_new5.visit_date < 30)] = '20 - 29'
    df_new5.frequency[(df_new5.visit_date >= 30) & (df_new5.visit_date < 40)] = '30 - 39'
    df_new5.frequency[(df_new5.visit_date >= 40) & (df_new5.visit_date < 50)] = '40 - 49'
    df_new5.frequency[(df_new5.visit_date >= 50)] = '50>='


    fig = px.bar(df_new3, orientation='v', text_auto='.2s',  height = 540, 
                title = 'Age demographic (during blood donation) of blood donors <br><sup>Total size = {:,}</sup>'.format(donors))
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    # fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False)
    st.write(fig)

    st.write("""# """)

    fig = px.bar(df_new1, orientation='v', text_auto='.2s',  height = 540, 
                title = 'Age demographic (as of 2024) of unique blood donors <br><sup>Total size = {:,}</sup>'.format(unique_donors))
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    # fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False)
    st.write(fig)
    
    st.write("""# """)
    
    fig = px.bar(df_new5.groupby('frequency')['donor_id'].sum(), orientation='v', text_auto='.2s',  height = 540, 
                title = 'Donation Frequency Among Blood Donors <br><sup>Total size = {:,}</sup>'.format(unique_donors))
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(xaxis = {'categoryorder':'array', 'categoryarray':['1', '2', '3 - 9','10 - 19', '20 - 29', '30 - 39', '40 - 49', '50>=']})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False)
    st.write(fig)

tab1, tab2, tab3 = st.tabs(["Latest daily trends", "Historical trends", "Blood retention trends"])

with tab1:
   yesterday_trends(df)

with tab2:
   historical_trends(df)

with tab3:
   retention_trends()



