import telebot
from telebot import types

data = {}
token = "5881944193:AAFjdxYqI6U_QG02s4UEMe10O84m0eC5BAU"
bot = telebot.TeleBot(token=token)
x = 0
y = 0
l = []
contents = ''
c = ''
@bot.message_handler(commands=["start"])
def start(message):
    # глобальная переменная, где сохранятеся статус для отдельного пользователя
    global data
    data.update({
        message.chat.id: {
            "status": x,
            "text": y,
        }
    })
    with open("text111.txt", "rb") as f:
        contents = f.read().decode("UTF-8")
    global l
    l = contents.split('/n')
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Далее", callback_data="button1")
    keyboard.add(button1)
    bot.send_photo(message.chat.id, 'https://ibb.co/WDNw9bq')
    bot.send_message(message.chat.id, text=l[0], reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        with open("text111.txt", "rb") as f:
            contents = f.read().decode("UTF-8")
        if data[call.message.chat.id]["text"] == 0:
            data[call.message.chat.id]["text"] = data[call.message.chat.id]["text"] + 1
        if call.data == "button1":
            if data[call.message.chat.id]["text"] != 22:
                keyboard = types.InlineKeyboardMarkup()
                button2 = types.InlineKeyboardButton(text="Далее", callback_data="button2")
                keyboard.add(button2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text=l[data[call.message.chat.id]['text']],
                                        reply_markup=keyboard)
                data[call.message.chat.id]["text"] = data[call.message.chat.id]["text"] + 1
            elif data[call.message.chat.id]["text"] == 22:
                keyboard1 = types.InlineKeyboardMarkup()
                button11 = types.InlineKeyboardButton(text="Излить", callback_data="button11")
                button22 = types.InlineKeyboardButton(text="Игнор", callback_data="button22")
                keyboard1.add(button11, button22)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=l[22], reply_markup=keyboard1)
                data[call.message.chat.id]["status"] = data[call.message.chat.id]["status"] + 1
        elif call.data == "button2":
            if data[call.message.chat.id]["text"] != 22:
                    keyboard = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text="Далее", callback_data="button1")
                    keyboard.add(button1)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=l[data[call.message.chat.id]['text']],
                                    reply_markup=keyboard)
                    data[call.message.chat.id]["text"] = data[call.message.chat.id]["text"] + 1
            elif data[call.message.chat.id]["text"] == 22:
                keyboard1 = types.InlineKeyboardMarkup()
                button11 = types.InlineKeyboardButton(text="Излить душу", callback_data="button11")
                button22 = types.InlineKeyboardButton(text="Проигнорировать", callback_data="button22")
                keyboard1.add(button11,button22)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=l[22], reply_markup=keyboard1)
                data[call.message.chat.id]["status"] = data[call.message.chat.id]["status"] + 1
        elif call.data == 'button11':
            print(data)
            with open("answerislit.txt", "rb") as f1:
                c = f1.read().decode("UTF-8")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=c)
        elif call.data == 'button22':
            print(data)
            with open("answerignor.txt", "rb") as f1:
                c = f1.read().decode("UTF-8")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=c)

bot.polling(none_stop=True)
