# legan
# A bot for Telegram that sends images through a list of uploaded image URLs.


import telebot
import picture
import random

from telebot import types


bot = telebot.TeleBot('TOKEN')  # токен
array = picture.pic

random_pic = lambda: random.choice(picture.pic)


# Старт бота с приветствием и созданием кнопок:
@bot.message_handler(commands=['start'])
def starting(message):
    # Создать кнопки:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Картинка')
    # Добавить кнопки:
    markup.add(btn)
    # Уведомить юзернейма о действиях, и возвести кнопки на экран
    bot.send_message(message.from_user.id, "Нажми на кнопку", reply_markup=markup)


# Реакция на действия юзернейма
@bot.message_handler(content_types=['text'])
def choose_one(message):
    print(message.text)
    if message.chat.type == 'private':
        if message.text == 'Картинка':
            bot.send_photo(message.from_user.id, random_pic())
        else:
            bot.send_message(message.from_user.id, 'Нужно нажать на кнопку, или написать аналогичный текст.')


bot.polling(none_stop=True)
