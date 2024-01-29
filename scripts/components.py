import pandas as pd
import streamlit as st
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import plotly.express as px 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from io import BytesIO
import requests
from styles.styles import kpi_box_malaysia, kpi_box_granular
from styles.styles import kpi_box_kuala_lumpur, kpi_box_kedah, kpi_box_perak, kpi_box_johor, kpi_box_sarawak, kpi_box_pulau_pinang, kpi_box_sabah, kpi_box_melaka
from styles.styles import kpi_box_selangor, kpi_box_negeri_sembilan, kpi_box_terengganu, kpi_box_pahang, kpi_box_kelantan, kpi_box_perlis, kpi_box_putrajaya, kpi_box_labuan
import time



def latest_trends(df, max_date):
    column = st.columns([7,2])
    column[0].write("""### Malaysia's Blood Donation Daily Updates (2024)""")
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
  
    tab1, tab2 = st.tabs(["Cumulative count of blood donations", "Latest daily count of blood donations"])

    with tab1:
        kpi_box_malaysia(malaysia_total)
        column = st.columns([1,1,1,1])

        column[0].markdown(kpi_box_johor(johor_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_kedah(kedah_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_kelantan(kelantan_total), unsafe_allow_html=True )
        column[3].markdown(kpi_box_melaka(melaka_total), unsafe_allow_html=True )

        column[0].markdown(kpi_box_negeri_sembilan(negeri_sembilan_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_pahang(pahang_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_perak(perak_total), unsafe_allow_html=True )
        column[3].markdown(kpi_box_perlis(0), unsafe_allow_html=True )

        column[0].markdown(kpi_box_pulau_pinang(pulau_pinang_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_sabah(sabah_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_sarawak(sarawak_total), unsafe_allow_html=True )
        column[3].markdown(kpi_box_selangor(selangor_total), unsafe_allow_html=True )

        column[0].markdown(kpi_box_terengganu(terengganu_total), unsafe_allow_html=True )
        column[1].markdown(kpi_box_kuala_lumpur(kuala_lumpur_total), unsafe_allow_html=True )
        column[2].markdown(kpi_box_labuan(0), unsafe_allow_html=True )
        column[3].markdown(kpi_box_putrajaya(0), unsafe_allow_html=True )
        

    with tab2:
        kpi_box_malaysia(malaysia)
        column = st.columns([1,1,1,1])
        column[0].markdown(kpi_box_johor(johor), unsafe_allow_html=True )
        column[1].markdown(kpi_box_kedah(kedah), unsafe_allow_html=True )
        column[2].markdown(kpi_box_kelantan(kelantan), unsafe_allow_html=True )
        column[3].markdown(kpi_box_melaka(melaka), unsafe_allow_html=True )

        column[0].markdown(kpi_box_negeri_sembilan(negeri_sembilan), unsafe_allow_html=True )
        column[1].markdown(kpi_box_pahang(pahang), unsafe_allow_html=True )
        column[2].markdown(kpi_box_perak(perak), unsafe_allow_html=True )
        column[3].markdown(kpi_box_perlis(0), unsafe_allow_html=True )

        column[0].markdown(kpi_box_pulau_pinang(pulau_pinang), unsafe_allow_html=True )
        column[1].markdown(kpi_box_sabah(sabah), unsafe_allow_html=True )
        column[2].markdown(kpi_box_sarawak(sarawak), unsafe_allow_html=True )
        column[3].markdown(kpi_box_selangor(selangor), unsafe_allow_html=True )

        column[0].markdown(kpi_box_terengganu(terengganu), unsafe_allow_html=True )
        column[1].markdown(kpi_box_kuala_lumpur(kuala_lumpur), unsafe_allow_html=True )
        column[2].markdown(kpi_box_labuan(0), unsafe_allow_html=True )
        column[3].markdown(kpi_box_putrajaya(0), unsafe_allow_html=True )

    
    st.write("""#####  """)

    fig = px.line(df[(df.state == 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', text = 'daily',
                   title = 'Time series of blood donors of Malaysia (YTD)')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='top center')
    # fig.write_image('./charts/malaysia_daily_{}.png'.format(max_date))
    st.write(fig)

    st.write("""######  """)

    fig = px.line(df[(df.state != 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', color = 'state',
                  title = 'Time series of blood donors across state (YTD)')
    # fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    # fig.write_image('./charts/state_daily_{}.png'.format(max_date))
    st.write(fig)


def historical_trends(df):
    df = df[df.year != '2024']

    column = st.columns([7,2])
    column[0].write("""### Malaysia's Blood Donation Yearly Trends (2006 - 2023)""")
    column[1].write("""  """)
    column[1].write("""  Data as of {}""".format(max(df.date)))

    malaysia_sum = df[df.state == 'Malaysia'].daily.sum()
    kpi_box_malaysia(malaysia_sum)

    fig = px.line(df[df.state == 'Malaysia'].groupby(['year','state'])['daily'].sum().reset_index(), x = 'year', y = 'daily', text = 'daily',
                 height = 540, title = 'Time series of blood donors by year across Malaysia (2006 - 2023)')
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='top center')
    st.write(fig)

    st.write("""##### """)

    fig = px.bar(df[df.state != 'Malaysia'].groupby('state')['daily'].sum(), orientation='h', text_auto='.2s',  height = 540, 
                title = 'Cumulative count of blood donors by state (2006 - 2023)',)
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_xaxes(showticklabels=False)
    st.write(fig)
    
    st.write("""##### """)

    fig = px.line(df[(df.state != 'Malaysia')].groupby(['year','state'])['daily'].sum().reset_index(), x = 'year', y = 'daily', color = 'state',
                 height = 540, title = 'Time series of blood donors across state of Malaysia (2006 - 2023)')
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
    st.write(fig)


def retention_trends():

    parquet_file_url = 'https://dub.sh/ds-data-granular'
    response = requests.get(parquet_file_url)
    parquet_data = BytesIO(response.content)
    df_granular = pq.read_pandas(parquet_data).to_pandas()
    df_granular.visit_date = pd.to_datetime(df_granular.visit_date).dt.date

    max_granular_date = max(df_granular.visit_date)

    column = st.columns([7,2])
    column[0].write("""### Malaysia's Blood Donors Retention Trends (2012 - 2024)""")
    column[1].write("""  """)
    column[1].write("""  Data as of {}""".format(max_granular_date))

    donors = len(df_granular.donor_id)
    unique_donors = len(df_granular.donor_id.unique())

    kpi_box_granular(donors, unique_donors)

    df_granular['visit_year'] = pd.to_datetime(df_granular.visit_date).dt.year
    df_granular['visit_age'] = df_granular.visit_year - df_granular.birth_date
    df_new = df_granular.groupby(['donor_id'])['birth_date'].mean().sort_values(ascending=False).reset_index()
    df_new['age'] = 2024 - df_new['birth_date']
    df_new['age_band'] = ''
    df_new.loc[df_new.age < 18, 'age_band'] = '0 - 17'
    df_new.loc[(df_new.age >= 18) & (df_new.age < 30), 'age_band'] = '18-29'
    df_new.loc[(df_new.age >= 30) & (df_new.age < 40), 'age_band'] = '30-39'
    df_new.loc[(df_new.age >= 40) & (df_new.age < 50), 'age_band'] = '40-49'
    df_new.loc[(df_new.age >= 50) & (df_new.age < 60), 'age_band'] = '50-59'
    df_new.loc[(df_new.age >= 60), 'age_band'] = '60>='
    df_new1  = df_new.groupby(['age_band'])['age_band'].count()

    df_new2 = df_granular
    df_new2['visit_age_band'] = ''
    df_new2.loc[df_new2.visit_age < 18, 'visit_age_band'] = '0 - 17'
    df_new2.loc[(df_new2.visit_age >= 18) & (df_new2.visit_age < 30), 'visit_age_band'] = '18-29'
    df_new2.loc[(df_new2.visit_age >= 30) & (df_new2.visit_age < 40), 'visit_age_band'] = '30-39'
    df_new2.loc[(df_new2.visit_age >= 40) & (df_new2.visit_age < 50), 'visit_age_band'] = '40-49'
    df_new2.loc[(df_new2.visit_age >= 50) & (df_new2.visit_age < 60), 'visit_age_band'] = '50-59'
    df_new2.loc[(df_new2.visit_age >= 60), 'visit_age_band'] = '60>='
    df_new3  = df_new2.groupby(['visit_age_band'])['visit_age_band'].count()


    df_new4 = df_granular.groupby('donor_id')['visit_date'].count().reset_index()
    df_new5 = df_new4.groupby('visit_date')['donor_id'].count().reset_index()
    df_new5.loc['frequency'] = df_new5.visit_date.astype('str')
    df_new5.loc[(df_new5.visit_date == 1), 'frequency'] = '1'
    df_new5.loc[(df_new5.visit_date == 2), 'frequency'] = '2'
    df_new5.loc[(df_new5.visit_date >= 3) & (df_new5.visit_date < 10), 'frequency'] = '3 - 9'
    df_new5.loc[(df_new5.visit_date >= 10) & (df_new5.visit_date < 20), 'frequency'] = '10 - 19'
    df_new5.loc[(df_new5.visit_date >= 20) & (df_new5.visit_date < 30), 'frequency'] = '20 - 29'
    df_new5.loc[(df_new5.visit_date >= 30) & (df_new5.visit_date < 40), 'frequency'] = '30 - 39'
    df_new5.loc[(df_new5.visit_date >= 40) & (df_new5.visit_date < 50), 'frequency'] = '40 - 49'
    df_new5.loc[(df_new5.visit_date >= 50), 'frequency'] = '50>='


    fig = px.bar(df_new3, orientation='v', text_auto='.2s',  height = 540, 
                title = 'Age demographic (during blood donation) of blood donors <br><sup>Total size = {:,}</sup>'.format(donors))
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    # fig.update_layout(yaxis = {"categoryorder":"total ascending"})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False)
    fig.write_image('./charts/blood_retention_age_whole_{}.png'.format(max_granular_date))
    st.write(fig)

    st.write("""##### """)

    fig = px.bar(df_new1, orientation='v', text_auto='.2s',  height = 540, 
                title = 'Age demographic (as of 2024) of unique blood donors <br><sup>Total size = {:,}</sup>'.format(unique_donors))
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False)
    fig.write_image('./charts/blood_retention_age_unique_{}.png'.format(max_granular_date))
    st.write(fig)
    
    st.write("""##### """)
    
    fig = px.bar(df_new5.groupby('frequency')['donor_id'].sum(), orientation='v', text_auto='.2s',  height = 540, 
                title = 'Donation Frequency Among Blood Donors <br><sup>Total size = {:,}</sup>'.format(unique_donors))
    fig.update_traces(showlegend = False)
    fig.update_layout(yaxis_title=None)
    fig.update_layout(xaxis_title=None)
    fig.update_layout(xaxis = {'categoryorder':'array', 'categoryarray':['1', '2', '3 - 9','10 - 19', '20 - 29', '30 - 39', '40 - 49', '50>=']})
    fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False)
    fig.write_image('./charts/blood_retention_frequency_{}.png'.format(max_granular_date))
    st.write(fig)


