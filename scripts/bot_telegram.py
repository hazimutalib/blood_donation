import telebot
import schedule
import time
from datetime import datetime, timedelta

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
