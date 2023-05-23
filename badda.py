# mengimport package pyTelegramBotAPI

import telebot

# inisialisasi Token Bot Kita

bot = telebot.TeleBot('5990596453:AAEwuGlra-ku5B5eU8qHUidZLeJWT5P5lEk')

# Menghandle Pesan /start

@bot.message_handler(commands=['start'])

def welcome(message):

    # membalas pesan

    bot.reply_to(message, 'Halo bro, ada apa?')

while True:

    try:

        bot.polling()

    except:

        pass
