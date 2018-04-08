import logging

import crickbotapi.bot.bot_logging
import circkbotapi.database.core as db

logger = logging.getLogger(__name__)

db.init_db_if_needed()


