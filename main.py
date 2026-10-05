import telebot
from logic import *
API_TOKEN = 'YOUR TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, я бот, показывающий состояние системы твоего компьютера.\
    """)


@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
/help, /start - Информация о боте.
/disk - Показывает информацию о диске.
/virtual_mem - Показывает количество используемой памяти
/cpu_count - Показывает количество логических и физических процессоров
/cpu_percent - Показывает загрузку процессора в процентах\
""")


@bot.message_handler(commands=['disk'])
def send_welcome(message):
    bot.reply_to(message, f"""{disk_info()}\
    """)

@bot.message_handler(commands=['virtual_mem'])
def send_welcome(message):
    bot.reply_to(message, f"""{virt_mem_info()}\
    """)

@bot.message_handler(commands=['cpu_count'])
def send_welcome(message):
    bot.reply_to(message, f"""{cpu_count()}\
    """)

@bot.message_handler(commands=['cpu_percent'])
def send_welcome(message):
    bot.reply_to(message, f"""{cpu_load_info()}\
    """)           


bot.infinity_polling()    