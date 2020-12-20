import telebot
from telebot import types

bot = telebot.TeleBot("890919990:AAGP8uEFbohWZ0V5u3K-wWkTDpwFITAd7JQ")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"Ещё раз приветстввую тебя, {message.from_user.first_name}\n"
                                      f"Я могу:\n"
                                      f"/start - начало работы\n"
                                      f"/help - помочь тебе в выборе команды\n"
                                      f"/settings - мои настройки(в стадии разработки)\n"
                                      f"/weather - дать тебе ссылку на прогноз погоды\n")


@bot.message_handler(commands=['settings'])
def settings(message):
    bot.send_message(message.chat.id, "Эта функция в стадии разработки")


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id,
                     'https://yandex.ru/pogoda/ryazan?utm_source=serp&utm_campaign=wizard&utm_medium=desktop&utm_content=wizard_desktop_main&utm_term=title&lat=54.63213&lon=39.651619')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == "hi" or "hello" or "привет" or "хай" or "йоу":
        bot.send_message(message.chat.id, 'Пиривет')

@bot.message_handler(commands=['riddle'])
def riddle(message):
    bot.send_message(message.chat.id,"Ооо, ты хочешь сыграть в загадки?")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да, я хочу сыграть в загадки", callback_data='Ok')
    item2 = types.InlineKeyboardButton("Нет, я случайно нажал на кнопку", callback_data='No')
    markup.add(item1, item2)





bot.polling(none_stop=True)
