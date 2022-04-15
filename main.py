import telebot
from telebot import types

bot = telebot.TeleBot("5333849077:AAFRoIYNrS-lnZnl1sAjSSfz9wYp4Vt7gt4")


@bot.message_handler(commands=["start"], chat_types=["private"])
def _start(msg):
    bot.send_message(msg.chat.id, "Hi bro.")


bot.infinity_polling(timeout=20)
