import telebot

API_TOKEN = '<api_token>'   #write here the API token, without it, the bot will not work

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Write here the phrase that the bot will say when the user click the command start\
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text=='write here the first phrase of the user':
        bot.reply_to(message, 'write here the answer of the bot')
    elif message.text=='write here the second phrase of the user':
        bot.reply_to(message, 'write here the answer of the bot')
    else:
        bot.reply_to(message, 'write here the answer of the bot if the user write something that the bot do not understand')

bot.polling()
