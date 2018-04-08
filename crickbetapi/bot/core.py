import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.bot import Bot

import crickbetapi.bot.bot_logging
import crickbetapi.database.core as db
import crickbetapi.constants as c

from crickbetapi.config import config
import callback as cb


logger = logging.getLogger(__name__)

# db.init_db_if_needed()

mybot = Bot(token=config.get('BOT_TOKEN', None))

updater = Updater(token=config.get('BOT_TOKEN', None))
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', cb.start)
help_handler = CommandHandler('help', cb.start)
message_handler = MessageHandler(Filters.text, cb.process_message)
unknown_handler = MessageHandler(Filters.command, cb.unknown)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()



