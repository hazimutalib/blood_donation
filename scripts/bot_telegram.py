import telebot

API_TOKEN = '6430193325:AAFkiOTYhb574_owPQVunkNHslzIxRAtNX8'
bot = telebot.TeleBot(API_TOKEN)

channel_id = '@blood_donatio'


try:
    bot.send_message(channel_id, 'Hello, World!')
    file_path = '.infographics/blood_donation.pdf'

    with open(file_path, 'rb') as file:
        bot.send_document(channel_id, file)

except:
    print('Message failed to send')
