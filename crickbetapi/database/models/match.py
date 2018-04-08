from sqlalchemy import Column, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class Match(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'matches'

    date = ''
    team_id_home = ''
    team_id_away = ''
    score_home = ''
    score_away = ''

