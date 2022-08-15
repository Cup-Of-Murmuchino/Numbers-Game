import random
from game import Session
import telebot
from telebot import types

question_personas = {}
bot = telebot.TeleBot("5333849077:AAFRoIYNrS-lnZnl1sAjSSfz9wYp4Vt7gt4")


@bot.message_handler(commands=["ask"])
def start_game(msg: types.Message):
    if msg.from_user.id not in question_personas.keys():
        question_personas.update({msg.from_user.id: 1})
        bot.send_message(msg.chat.id, "Ответь.")
    else:
        bot.send_message(msg.chat.id, "Ты уже спросил.")


@bot.message_handler(content_types=["text"])
def get_answer(msg: types.Message):
    print("message")
    if msg.from_user.id in question_personas.keys():
        bot.send_message(msg.chat.id, f"@{msg.from_user.username} твой ответ: {msg.text} ")
        question_personas.pop(msg.from_user.id)


# @bot.callback_query_handler(func=lambda call: True)
# def callback(call: types.CallbackQuery):
#     if call.data == "join":
#         bot.send_message(call.message.chat.id, "You click a button.")


# def new_game_id():
#     used_ids = []
#     id_threat = 1234
#     for thread in threading.enumerate():
#         used_ids.append(thread.getName())
#     while id_threat in used_ids:
#         threat = 0
#         for i in range(0, 4):
#             threat += random.randint(1, 9) * pow(10, i)
#         id_threat = threat
#     return str(id_threat)


bot.infinity_polling(timeout=20)
