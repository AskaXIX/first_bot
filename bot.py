# import telebot
# import requests

# bot = telebot.TeleBot(token="5799740294:AAGEaQWKyGOUKUd4m0f9nnjuyp5iN2Nemd4")

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет! Я бот для поиска информации в Google. Напиши мне свой запрос и я помогу тебе с поиском!')

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     query = message.text
#     r = requests.get('https://www.google.com/search?q='+query)
#     bot.send_message(message.chat.id, r.url)

# bot.polling()


import telebot
from googlesearch import search

bot = telebot.TeleBot(token="5799740294:AAGEaQWKyGOUKUd4m0f9nnjuyp5iN2Nemd4")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для поиска информации в Google. Напиши мне свой запрос и я помогу тебе с поиском!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    query = message.text
    try:
        search_results = list(search(query, num=1, stop=1, pause=2.0))
        if search_results:
            bot.send_message(message.chat.id, "Вот результаты поиска:")
            for result in search_results:
                bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "По вашему запросу ничего не найдено.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

bot.polling()
