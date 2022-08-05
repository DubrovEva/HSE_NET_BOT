import telebot

token = open("resources/token.txt", "r").read()
bot = telebot.TeleBot(token=token)

bot.polling(none_stop=True)