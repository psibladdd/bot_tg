from telebot import *
import random

bot = telebot.TeleBot("6501265855:AAFVuQtzQAQVgR-xYnaGZ2zykf5lk_S2dvw")

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, f'Хеллоу, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.chat.id, 'Текст с инфой')

@bot.message_handler(commands=['mark'])
def info(message):
    type = types.InlineKeyboardMarkup()
    type.add(types.InlineKeyboardButton('Фото'))
    bot.send_message(message.chat.id, 'Выбери что надо оценить',reply_markup=type)




@bot.message_handler()
def text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Че хотел, епта')
    else:
        bot.send_message(message.chat.id, 'Не вдупляю, сори')

bot.polling(none_stop=True)

@bot.message_handler()
def photo_mark(message):
    x = random.randint(0,5)
    if(x==0): bot.send_message(message.chat.id, 'Уфф, какой')
    elif(x==2): bot.send_message(message.chat.id, 'Милашка господи')
    elif (x == 3): bot.send_message(message.chat.id, 'АААААА НЕФОРЫ')
    elif (x == 4): bot.send_message(message.chat.id, 'Вижу, что он пидор')