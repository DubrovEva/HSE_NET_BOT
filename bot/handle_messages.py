import telebot

import bot

@bot.message_handler(content_types=['text'])
def text_response(message):
    text = message.text
    user = message.chat.id

    bot.send_sticker(user, "CAACAgIAAxkBAAEFYiRi3_xKlJaqNPHTcUu5w4hSrR_TtAAClgEAAlERmR-WRNMOCbPRrCkE")


@bot.message_handler(commands=['start'])
def start_command(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['register'])
def help_command(message):
	bot.reply_to(message, "Please, enter your name")

    

bot.polling(none_stop=True)