import logging

from crickbetapi.config import config
from crickbetapi.database.models.metadata.common import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__name__)

engine = None # create_engine(config.get('DB_URI')

# Base.metadata.create_all(engine)
session_maker = None # sessionmaker(bind=engine)
session = None # session_maker()

def init_session():
    global session_maker
    global session
    global engine

    if engine is None:
        engine = create_engine(config.get('DB_URI'))

    if session_maker is None:
        session_maker = sessionmaker(bind=engine)

    if session is None:
        session = session_maker()

    Base.metadata.create_all(engine)

def init_db():
    pass

def init_db_if_needed():
    global session

    if session is None:
        init_session()
        init_db()

