import pandas as pd
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import plotly.express as px 
from datetime import datetime, timedelta
import pytz
from scripts.edit_powerpoint import edit_powerpoint_template
import time
import telebot
from spire.presentation import Presentation as Presentation2, FileFormat
import os
from io import BytesIO
import requests


donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"
df = pd.read_csv(donations_state_url)
df.date = pd.to_datetime(df.date).dt.date
df['year'] = df['date'].astype('str').apply(lambda x: x[:4])
max_date = max(df.date)



df = df[df.year == '2024']

negeri_total_value = [df[(df.state == "{}".format(x))].daily.sum() for x in sorted(df.state.unique())]
[johor_total, kedah_total, kelantan_total, malaysia_total, melaka_total, negeri_sembilan_total, 
pahang_total, perak_total, pulau_pinang_total, sabah_total, sarawak_total, selangor_total, 
terengganu_total, kuala_lumpur_total] = negeri_total_value

negeri_value = [df[(df.date == df.date.max()) & (df.state == "{}".format(x))].daily.iloc[0] for x in sorted(df.state.unique())]
[johor, kedah, kelantan, malaysia, melaka, negeri_sembilan, 
pahang, perak, pulau_pinang, sabah, sarawak, selangor, 
terengganu, kuala_lumpur] = negeri_value


image1_path = './charts/malaysia_daily_{}.png'.format(max_date)
image2_path = './charts/state_daily_{}.png'.format(max_date)

fig = px.line(df[(df.state == 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', text = 'daily',
                   title = 'Time series of blood donors of Malaysia (YTD)')
fig.update_traces(showlegend = False)
fig.update_layout(yaxis_title=None)
fig.update_layout(xaxis_title=None)
fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
fig.update_traces(texttemplate='%{text:.2s}', textposition='top center')
fig.write_image(image1_path)
print('Chart 1 is generated')

fig = px.line(df[(df.state != 'Malaysia')].groupby(['date','state'])['daily'].sum().reset_index(), x = 'date', y = 'daily', color = 'state',
                  title = 'Time series of blood donors across state (YTD)')
    # fig.update_traces(showlegend = False)
fig.update_layout(yaxis_title=None)
fig.update_layout(xaxis_title=None)
fig.update_layout(plot_bgcolor='white', paper_bgcolor = 'white')
fig.write_image(image2_path)
print('Chart 2 is generated')


parquet_file_url = 'https://dub.sh/ds-data-granular'
response = requests.get(parquet_file_url)
parquet_data = BytesIO(response.content)
df_granular = pq.read_pandas(parquet_data).to_pandas()
df_granular.visit_date = pd.to_datetime(df_granular.visit_date).dt.date
max_granular_date = max(df_granular.visit_date)

image3_path = './charts/blood_retention_age_total_{}.png'.format(max_granular_date)
image4_path = './charts/blood_retention_age_unique_{}.png'.format(max_granular_date)
image5_path = './charts/blood_retention_frequency_{}.png'.format(max_granular_date)

donors = len(df_granular.donor_id)
unique_donors = len(df_granular.donor_id.unique())

df_granular['visit_year'] = pd.to_datetime(df_granular.visit_date).dt.year
df_granular['visit_age'] = df_granular.visit_year - df_granular.birth_date

df_new = df_granular.groupby(['donor_id'])['birth_date'].mean().sort_values(ascending=False).reset_index()
df_new['age'] = 2024 - df_new['birth_date']
df_new['age_band'] = ''


# df_new.age_band[df_new.age < 18] = '0 - 17'
# df_new.age_band[(df_new.age >= 18) & (df_new.age < 30)] = '18-29'
# df_new.age_band[(df_new.age >= 30) & (df_new.age < 40)] = '30-39'
# df_new.age_band[(df_new.age >= 40) & (df_new.age < 50)] = '40-49'
# df_new.age_band[(df_new.age >= 50) & (df_new.age < 60)] = '50-59'
# df_new.age_band[(df_new.age >= 60)] = '60>='
# df_new1  = df_new.groupby(['age_band'])['age_band'].count()

# df_new2 = df_granular
# df_new2['visit_age_band'] = ''
# df_new2.visit_age_band[df_new2.visit_age < 18] = '0 - 17'
# df_new2.visit_age_band[(df_new2.visit_age >= 18) & (df_new2.visit_age < 30)] = '18-29'
# df_new2.visit_age_band[(df_new2.visit_age >= 30) & (df_new2.visit_age < 40)] = '30-39'
# df_new2.visit_age_band[(df_new2.visit_age >= 40) & (df_new2.visit_age < 50)] = '40-49'
# df_new2.visit_age_band[(df_new2.visit_age >= 50) & (df_new2.visit_age < 60)] = '50-59'
# df_new2.visit_age_band[(df_new2.visit_age >= 60)] = '60>='
# df_new3  = df_new2.groupby(['visit_age_band'])['visit_age_band'].count()

# df_new4 = df_granular.groupby('donor_id')['visit_date'].count().reset_index()
# df_new5 = df_new4.groupby('visit_date')['donor_id'].count().reset_index()
# df_new5['frequency'] = df_new5.visit_date.astype('str')
# df_new5.frequency[(df_new5.visit_date == 1)] = '1'
# df_new5.frequency[(df_new5.visit_date == 2)] = '2'
# df_new5.frequency[(df_new5.visit_date >= 3) & (df_new5.visit_date < 10)] = '3 - 9'
# df_new5.frequency[(df_new5.visit_date >= 10) & (df_new5.visit_date < 20)] = '10 - 19'
# df_new5.frequency[(df_new5.visit_date >= 20) & (df_new5.visit_date < 30)] = '20 - 29'
# df_new5.frequency[(df_new5.visit_date >= 30) & (df_new5.visit_date < 40)] = '30 - 39'
# df_new5.frequency[(df_new5.visit_date >= 40) & (df_new5.visit_date < 50)] = '40 - 49'
# df_new5.frequency[(df_new5.visit_date >= 50)] = '50>='


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
fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
fig.update_yaxes(showticklabels=False)
fig.update_yaxes(showgrid=False)
fig.write_image(image3_path)
print('Chart 3 is generated')


fig = px.bar(df_new1, orientation='v', text_auto='.2s',  height = 540, 
            title = 'Age demographic (as of 2024) of unique blood donors <br><sup>Total size = {:,}</sup>'.format(unique_donors))
fig.update_traces(showlegend = False)
fig.update_layout(yaxis_title=None)
fig.update_layout(xaxis_title=None)
fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
fig.update_yaxes(showticklabels=False)
fig.update_yaxes(showgrid=False)
fig.write_image(image4_path)
print('Chart 4 is generated')

fig = px.bar(df_new5.groupby('frequency')['donor_id'].sum(), orientation='v', text_auto='.2s',  height = 540, 
            title = 'Donation Frequency Among Blood Donors <br><sup>Total size = {:,}</sup>'.format(unique_donors))
fig.update_traces(showlegend = False)
fig.update_layout(yaxis_title=None)
fig.update_layout(xaxis_title=None)
fig.update_layout(xaxis = {'categoryorder':'array', 'categoryarray':['1', '2', '3 - 9','10 - 19', '20 - 29', '30 - 39', '40 - 49', '50>=']})
fig.update_layout(plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor = "rgba(255,255,255,1)")
fig.update_yaxes(showticklabels=False)
fig.update_yaxes(showgrid=False)
fig.write_image(image5_path)
print('Chart 5 is generated')


path_to_check = './infographic/blood_donation_{}.pdf'.format(max_date)

utc_now = datetime.utcnow()
utc_timezone = pytz.utc
utc_now = utc_timezone.localize(utc_now)
gmt8_timezone = pytz.timezone('Asia/Singapore')
today_date = utc_now.astimezone(gmt8_timezone).date()
difference = today_date - max_date
print('Check the existence of file')
if (difference.days == 2) & (not os.path.exists(path_to_check)):
    template_path = './blood_donation.pptx'
    file_path = './infographic/blood_donation_{}.pptx'.format(max(df.date))


    edit_powerpoint_template(template_path, file_path, malaysia_total, kuala_lumpur_total, kedah_total, 
                        perak_total, johor_total, sarawak_total, pulau_pinang_total, sabah_total, melaka_total, selangor_total, 
                        negeri_sembilan_total, terengganu_total, pahang_total, kelantan_total, max_date, malaysia, kuala_lumpur, kedah, 
                        perak, johor, sarawak, pulau_pinang, sabah, melaka, selangor, negeri_sembilan, terengganu, pahang, kelantan, 
                        image1_path, image2_path, image3_path, image4_path, image5_path, donors, unique_donors, max_granular_date)

    file_path_pdf = './infographic/blood_donation_{}.pdf'.format(max_date)
    presentation2 = Presentation2()
    presentation2.LoadFromFile(file_path)
    presentation2.SaveToFile(file_path_pdf, FileFormat.PDF)
    # presentation2.Dispose()

    print(f"Edited pdf saved to {file_path_pdf}")

    tkn = '6407333558:AAE7og0l5ufBd-LVi0xlgLyDX3swnLGSVY8'

    bot = telebot.TeleBot(tkn)

    channel_id = '@hazim_mutalib_blood_donation'
    message = """
    🩸 **Blood Donation Update of 2024 - Data as of {}** 🩸
    📈 Today's Blood Donation Count:
    - Total Donations: {:,}
    - Latest Daily Donations: {:,}

    Thank you to all donors for making a difference! 💖
    #BloodDonation #DonateLife #SaveLives

                    """.format(max_date, malaysia_total, malaysia)
    try:
        with open(file_path_pdf, 'rb') as file:
            bot.send_document(channel_id, file)
        bot.send_message(channel_id, message, parse_mode='Markdown')        
    except:
        bot.send_message(channel_id, 'File failed to send', parse_mode='Markdown')


else:
    print('File already exist')


