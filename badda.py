# mengimport package pyTelegramBotAPI

import telebot

# inisialisasi Token Bot Kita

bot = telebot.TeleBot('TOKENKALIAN')

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
