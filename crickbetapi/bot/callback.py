import logging

from crickbetapi.config import config
from parser import BetParser


logger = logging.getLogger(__name__)

parser = BetParser()

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


def start(bot, update):
    chat_id = config.get('GROUP_CHAT_ID', update.message.chat_id)
    text = "I'm a bot, please talk to me!"

    bot.send_message(chat_id=chat_id, text=text)


def help(bot, update):
    chat_id = config.get('GROUP_CHAT_ID', update.message.chat_id)
    text = 'test help'

    bot.send_message(chat_id=chat_id, text=text)

def unknown(bot, update):
    chat_id = config.get('GROUP_CHAT_ID', update.message.chat_id)
    text = "Sorry, I didn't understant that command."

    bot.send_message(chat_id=chat_id, text=text)



