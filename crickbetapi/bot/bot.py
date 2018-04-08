import logging

from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from crickbetapi.config import config, teams
from parser import BotParser

import crickbetapi.constants as c



updater = Updater(token=config.get('BOT_TOKEN', None))
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="test help")

help_handler = CommandHandler('help', start)
dispatcher.add_handler(help_handler)

parser = BotParser()

def process_message(bot, update):
    chat_id = update.message.chat_id
    effective_message = update.effective_message
    effective_user = update.effective_user
    message = update.message
    update_id = update.update_id
    
    # check if update is from master
    # do some action as per master instructions
    if update.message.chat_id == config.get('MASTER_CHAT_ID', 557058075):
        pass

    if update.message.chat_id == config.get('TEST_CHAT_ID', -272845684):
        pass

    if update.message.chat_id == config.get('GROUP_CHAT_ID', 0):
        pass
    # pass update to parser
    parser.parse(update)
    
message_handler = Messagehandler(Filters.text, process_message)
dispatcher.add_handler(message_handler)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
