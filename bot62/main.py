# -*- coding: utf-8 -*-
import telebot
import losev/knb

token = "LaLaLaLaLa"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['Start'])
def on_message(message):
  bot.send_message(message.chat.id, 'Здравствуйте! Я совместое создание группы\n'
                                     'ТМП-61 bot61 v1.0. Что я умею делать:\n'
                                     '__________________________________________________\n'
                                     'помочь поиграть двум людям в камень-ножницы-бумагу\n'
                                     'просто напиши /game и следуй командам бота\n'
                                     'не жми на кнопки клавиатуры слишком часто - бот может ненадоло задуматься\n'
                                     '__________________________________________________\n'
                                     '-- blablabla')

if __name__ == "__main__":
    bot.polling(none_stop=True)
