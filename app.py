import pandas as pd
import streamlit as st
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import plotly.express as px 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from io import BytesIO
import requests
from styles.styles import kpi_box_malaysia, kpi_box_1, kpi_box_2, kpi_box_3, kpi_box_4, kpi_box_css, body_css, kpi_box_granular
from scripts.upload_pptx_to_github import upload_pptx_to_github

from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
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



def historical_trends(df):
    
    column = st.columns([1,1,1])
    state = column[0].multiselect('State:', df[df.state != 'Malaysia'].state.unique())
    date = column[1].date_input('Range of date:', value = (min(df.date), max(df.date)))

    st.write("""###### Data is updated as of {}""".format(max(df.date)))

    if date[0] != min(df.date):
        try:
            st.write("""### Malaysia's Blood Donation Trends from {} to {}""".format(date[0], date[0]))
        except:
            st.write("""### Malaysia's Blood Donation Trends from {} to {}""".format(date[0], date[1]))
    else:
        st.write("""### Malaysia's Blood Donation Trends from 2012 to 2024""".format(max(df.date)))

    df_new = df

    if not state:
        df = df
        df_new = df_new[(df_new.state == "Malaysia")]
    else: 
        df = df[df.state.isin(state)]
        df_new = df_new[df_new.state.isin(state)]

    try:
        df = df[(df.date >= date[0]) & (df.date <= date[1])]
        df_new = df_new[(df_new.date >= date[0]) & (df_new.date <= date[1])]
        
    except:
        df = df
        df_new = df_new
        

    malaysia_sum = df_new.daily.sum()

    kpi_box_malaysia(malaysia_sum)

    column = st.columns([5,1,5,1,5])

    fig = px.bar(df[df.state != 'Malaysia'].groupby('state')['daily'].sum(), orientation='h', text_auto='.2s', width = 360, height = 500, 
                title = 'Blood donors by state',)
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_xaxes(showticklabels=False)
    column[0].write(fig)


    fig = px.line(df_new.groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily',
                width = 360, height = 500, title = 'Time series of blood donors of Malaysia')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    column[2].write(fig)


    fig = px.line(df[(df.state != 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', color = 'state',
                width = 360, height = 500, title = 'Time series of blood donors across state')
    # fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    column[4].write(fig)



def yesterday_trends(df):
    st.write("""### Malaysia's Blood Donation Count on {}""".format(max(df.date)))
    malaysia = df[(df.date == df.date.max()) & (df.state == "Malaysia")].daily
    kedah = df[(df.date == df.date.max()) & (df.state == "Kedah")].daily
    pulau_pinang = df[(df.date == df.date.max()) & (df.state == "Pulau Pinang")].daily
    perak = df[(df.date == df.date.max()) & (df.state == "Perak")].daily
    selangor = df[(df.date == df.date.max()) & (df.state == "Selangor")].daily
    kuala_lumpur = df[(df.date == df.date.max()) & (df.state == "W.P. Kuala Lumpur")].daily
    negeri_sembilan = df[(df.date == df.date.max()) & (df.state == "Negeri Sembilan")].daily
    putrajaya = df[(df.date == df.date.max()) & (df.state == "W.P. Putrajaya")].daily
    sabah = df[(df.date == df.date.max()) & (df.state == "Sabah")].daily
    sarawak = df[(df.date == df.date.max()) & (df.state == "Sarawak")].daily
    kelantan = df[(df.date == df.date.max()) & (df.state == "Kelantan")].daily
    terengganu= df[(df.date == df.date.max()) & (df.state == "Terengganu")].daily
    pahang = df[(df.date == df.date.max()) & (df.state == "Pahang")].daily
    melaka = df[(df.date == df.date.max()) & (df.state == "Melaka")].daily
    johor = df[(df.date == df.date.max()) & (df.state == "Johor")].daily


    # malaysia_sum = df[(df.date > '2013-12-31') & (df.state == "Malaysia")].daily.sum()
    # kedah_sum = df[(df.date > '2013-12-31') & (df.state == "Kedah")].daily.sum()
    # pulau_pinang_sum = df[(df.date > '2013-12-31') & (df.state == "Pulau Pinang")].daily.sum()
    # perak_sum = df[(df.date > '2013-12-31') & (df.state == "Perak")].daily.sum()
    # selangor_sum = df[(df.date > '2013-12-31') & (df.state == "Selangor")].daily.sum()
    # kuala_lumpur_sum = df[(df.date > '2013-12-31') & (df.state == "W.P. Kuala Lumpur")].daily.sum()
    # negeri_sembilan_sum = df[(df.date > '2013-12-31') & (df.state == "Negeri Sembilan")].daily.sum()
    # putrajaya_sum = df[(df.date > '2013-12-31') & (df.state == "W.P. Putrajaya")].daily.sum()
    # sabah_sum = df[(df.date > '2013-12-31') & (df.state == "Sabah")].daily.sum()
    # sarawak_sum = df[(df.date > '2013-12-31') & (df.state == "Sarawak")].daily.sum()
    # kelantan_sum = df[(df.date > '2013-12-31') & (df.state == "Kelantan")].daily.sum()
    # terengganu_sum= df[(df.date > '2013-12-31') & (df.state == "Terengganu")].daily.sum()
    # pahang_sum = df[(df.date  > '2013-12-31') & (df.state == "Pahang")].daily.sum()
    # melaka_sum = df[(df.date  > '2013-12-31') & (df.state == "Melaka")].daily.sum()
    # johor_sum = df[(df.date > '2013-12-31') & (df.state == "Johor")].daily.sum()


    # st.write('Data shown count of blood donors on {}'.format(max(df.date)))
    kpi_box_malaysia(malaysia.iloc[0])
    kpi_box_1(kuala_lumpur.iloc[0], kedah.iloc[0], perak.iloc[0], johor.iloc[0])
    kpi_box_2(sarawak.iloc[0], pulau_pinang.iloc[0], sabah.iloc[0], melaka.iloc[0])
    kpi_box_3(selangor.iloc[0], negeri_sembilan.iloc[0], terengganu.iloc[0], pahang.iloc[0])
    kpi_box_4(kelantan.iloc[0], 0, 0, 0)

    # st.write('Data as of {}'.format(max(df.date)))
    # kpi_box_malaysia(malaysia_sum)
    # kpi_box_1(kedah_sum, pulau_pinang_sum, perak_sum, selangor_sum)
    # kpi_box_2(kuala_lumpur_sum, negeri_sembilan_sum, sabah_sum, sarawak_sum)
    # kpi_box_3(kelantan_sum, terengganu_sum, pahang_sum, melaka_sum)
    # kpi_box_4(johor_sum, 0, 0, 0)

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

    file_path_pdf = './infographic/output_test.pdf'
    presentation2 = Presentation2()
    presentation2.LoadFromFile(file_path)
    presentation2.SaveToFile(file_path_pdf, FileFormat.PDF)
    # presentation2.Dispose()

    upload_pptx_to_github(repo_owner, repo_name, template_path, file_path_pdf, lol)
