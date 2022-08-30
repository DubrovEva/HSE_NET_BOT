import telebot

token = open("resources/token.txt", "r").read()
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def text_response(message):
    text = message.text
    user = message.chat.id

    bot.send_sticker(user, "CAACAgIAAxkBAAEFYiRi3_xKlJaqNPHTcUu5w4hSrR_TtAAClgEAAlERmR-WRNMOCbPRrCkE")


bot.polling(none_stop=True)
