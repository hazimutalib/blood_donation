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
from spire.presentation import Presentation as Presentation2, FileFormat


st.set_page_config(layout="wide")

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
df = df[df.date > '2011-12-31']
df.date = pd.to_datetime(df.date).dt.date
df['year'] = df['date'].astype('str').apply(lambda x: x[:4])



def historical_trends(df):
    df = df[df.year != '2024']

    column = st.columns([9,1])
    column[0].write("""### Malaysia's Blood Donation Trends from 2012 to 2023""")
    column[1].write("""###### Data as of {}""".format(max(df.date)))


    malaysia_sum = df[df.state == 'Malaysia'].daily.sum()

    kpi_box_malaysia(malaysia_sum)

    column = st.columns([1,4,1,4,1])

    fig = px.line(df[df.state == 'Malaysia'].groupby(['year','state'])['daily'].sum().reset_index(), x = 'year', y = 'daily',
                width = 540, height = 540, title = 'Count of blood donors by year across Malaysia (2012-2023)')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    st.write(fig)

    fig = px.bar(df[df.state != 'Malaysia'].groupby('state')['daily'].sum(), orientation='h', text_auto='.2s', width = 540, height = 540, 
                title = 'Cumulative count of blood donors by state (2012-2023)',)
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_xaxes(showticklabels=False)
    st.write(fig)


    
    column[1].write("""# """)

    column = st.columns([3,4,3])
    fig = px.line(df[(df.state != 'Malaysia')].groupby(['year','state'])['daily'].sum().reset_index(), x = 'year', y = 'daily', color = 'state',
                 height = 540, title = 'Count of blood donors by year across state of Malaysia (2012-2023)')
    # fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    st.write(fig)



def yesterday_trends(df):
    column = st.columns([9,1])
    column[0].write("""### Malaysia's Blood Donation Daily Updates (2024)""")
    column[1].write("""###### Data as of {}""".format(max(df.date)))

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
    column = st.columns([1,4,1,4,1])

    fig = px.line(df[(df.state == 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', 
                  width = 540 , title = 'Time series of blood donors of Malaysia (YTD)')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    column[1].write(fig)


    fig = px.line(df[(df.state != 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', color = 'state',
                 width = 540, title = 'Time series of blood donors across state (YTD)')
    # fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    
    column[3].write(fig)





def retention_trends(df):
    st.write("""### Malaysia's Blood Donors Retention Trends for the past 6 months""")
    st.write("""##### Regular donors are individuals who have made more than one blood donation within the last 6 months as of the latest date in the dataset""")
    
    parquet_file_url = 'https://dub.sh/ds-data-granular'
    response = requests.get(parquet_file_url)
    parquet_data = BytesIO(response.content)
    df_granular = pq.read_pandas(parquet_data).to_pandas()
    df_granular.visit_date = pd.to_datetime(df_granular.visit_date).dt.date
    df_granular = df_granular[df_granular.visit_date >= max(df_granular.visit_date) - relativedelta(months=6)]
    st.write('The 6 months period are from {} to {}'.format(min(df_granular.visit_date), max(df_granular.visit_date)))

    donors_aggregated = df[(df.state == 'Malaysia')].daily.sum()
    donors = len(df_granular.donor_id)
    unique_donors = len(df_granular.donor_id.unique())
    pre_regular_donors = df_granular.groupby('donor_id')['visit_date'].count().sort_values(ascending=False).reset_index()
    pre_regular_donors1 = pre_regular_donors.groupby('visit_date')['donor_id'].count().reset_index()
    regular_donors = pre_regular_donors1[pre_regular_donors1.visit_date >= 2].donor_id.sum()

  
    

    # fig = px.bar(lol1, orientation='h', text_auto='.2s', width = 440, height = 500, 
    #             title = 'Blood donors by state (2012 - 2024)')
    # fig.update_traces(showlegend = False)
    # fig.update_layout(yaxis_title=None)
    # fig.update_layout(xaxis_title=None)
    # # fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    # fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    # fig.update_xaxes(showticklabels=False)
    # column[0].write(fig)
    kpi_box_granular(donors, unique_donors, regular_donors, regular_donors/unique_donors)

    # st.write(df_granular)
    # st.write(donors_aggregated)
    # st.write(donors)
    # st.write(unique_donors)

tab1, tab2, tab3 = st.tabs(["Latest daily update", "Historical trends", "Blood retention trends"])

with tab1:
   yesterday_trends(df)

with tab2:
   historical_trends(df)

with tab3:
   retention_trends(df)


if st.button('Upload'):
    repo_owner = 'hazimutalib'
    repo_name = 'blood_donation'
    template_path = './blood_donation.pptx'
    file_path = './infographic/output_test.pptx'
    lol = 'ghp_XQuAk8BlOgV2PNLwq3qWbuMG0DwuQI46YKk0'
    
    lol = lol.replace('2','1').replace('3','2').replace('4','3').replace('6','5')


    upload_pptx_to_github(repo_owner, repo_name, template_path, file_path, lol)
    
    time.sleep(5)

    file_path_pdf = './infographic/output_test.pdf'
    presentation2 = Presentation2()
    presentation2.LoadFromFile(file_path)
    presentation2.SaveToFile(file_path_pdf, FileFormat.PDF)
    presentation2.Dispose()

    # PDFConverter().convert(presentation2, file_path_pdf)
    upload_pdf_to_github(file_path_pdf, lol, repo_owner, repo_name)
    # upload_pptx_to_github(repo_owner, repo_name, template_path, file_path_pdf, lol)
