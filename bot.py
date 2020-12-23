from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import TG_TOKEN
from pprint import pprint

def sms(bot, update):
    print(" Pushing /start !")
    bot.message.reply_text('Hi {} i`m stupid one...'.format(bot.message.chat.first_name))
    print(bot.message)

def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)

def main():
    my_bot = Updater(TG_TOKEN, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start',sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text,parrot))
    my_bot.start_polling()
    my_bot.idle()

main()