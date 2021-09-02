from transliterate import to_cyrillic as kril,to_latin as lotin
import telebot
TOKEN = '1841513867:AAHanz0o09DtKFAnXTvHE10NmQM8yYXbHfU'
bot = telebot.TeleBot(TOKEN,parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = 'Assalomu alaykum xush kelibsiz!'
    javob += '\nMatnni kiriting'
    bot.reply_to(message,javob)
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'Assalomu alaykum Qanday yordam kerak?')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: kril(msg) if msg.isascii() else lotin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()