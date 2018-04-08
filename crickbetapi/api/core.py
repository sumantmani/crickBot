import logging

import crickbotapi.api.resources as r
import crickbotapi.database.core as db

import crickbotapi.api.api_logging

logger = logging.getLogger(__name__)

db.init_db_if_needed()


