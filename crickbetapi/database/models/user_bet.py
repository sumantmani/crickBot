from sqlalchemy import Column, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class UserBet(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'user_bets'

    match_id = 
    outcome = ''


