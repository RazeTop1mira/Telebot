from telebot import TeleBot
from telebot import types
from weekdays import week
from TOKEN import token
from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Document, InputMediaDocument, File
from rps_func import rps_check
from timetable_func import timetable_checker
from userid_func import userid_func

bot = TeleBot(token)



key1 = InlineKeyboardMarkup()
key1.add(
    InlineKeyboardButton("Камень"),
    InlineKeyboardButton("Ножницы"),
    InlineKeyboardButton("Бумага")
)

key2 = ReplyKeyboardMarkup()
key2.row(
    KeyboardButton("Камень"),
    KeyboardButton("Ножницы"),
    KeyboardButton("Бумага")
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуй, я бот созданный с целью загрузки и отображения расписания. Или можем поиграть в камень, ножницы, бумага")


@bot.message_handler(commands=['rps'])
def message_command_rps(msg: types.Message):
    bot.send_message(msg.chat.id, "Давай сыграем в камень, ножницы, бумага", reply_markup=key2)



@bot.message_handler(commands=['timetable'])
def message_command_timetable(message):
    markup_inline = InlineKeyboardMarkup(row_width=1)
    for key in week:
        item = InlineKeyboardButton(text=key, callback_data=f'расписание {key}')
        markup_inline.add(item)
    bot.send_message(message.chat.id, 'Выбери день:', reply_markup=markup_inline)

@bot.message_handler(commands=['timetablechange'])
def message_command_timetable(message):
    username = message.from_user.username
    bot.send_message(message.chat.id, 'Пришли файл в формате .txt и вида:\nТвой файл должен выглядеть также, как присланный ниже')
    doc = open('texts/text0.txt', 'rb')
    bot.send_document(message.chat.id, doc)
    doc.close()
    @bot.message_handler(content_types=["document"])
    def content_document(message):

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'texts/text' + str(message.chat.id) +'.txt'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        print('Saved')
        bot.send_message(message.chat.id, 'Спасибо, ваше расписание сохранено')

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data.split()[0] == 'расписание':
        bot.send_message(call.message.chat.id, timetable_checker(call.data, call.message.chat.id, 0))

@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    msg = message
    userid = userid_func(msg.chat.id, msg.from_user.username)
    if (msg.text == "Камень" or msg.text == "Ножницы" or msg.text == "Бумага"):
        key_del = ReplyKeyboardRemove()
        bot.send_message(msg.chat.id, rps_check(msg.text), reply_markup=key_del)
    elif (msg.text.split()[0] == "Расписание") or (msg.text.split()[0] == "расписание"):
        if isinstance(timetable_checker(msg.text, msg.chat.id, msg.from_user.username), str):
            bot.send_message(msg.chat.id, timetable_checker(msg.text, msg.chat.id, msg.from_user.username))
        else:
            bot.send_message(msg.chat.id, timetable_checker(msg.text, msg.chat.id, msg.from_user.username))
    else:
        print(msg.text, msg.chat.id, msg.from_user.username)




if __name__ == "__main__":

    bot.polling(none_stop=True)