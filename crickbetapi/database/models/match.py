from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from .metadata.common import Base
from .metadata.mixins import GUID, HasCreatedAt, HasUpdatedAt, HasUUIDID

class Match(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'matches'

    date = Column(Date)

    team_id_home = Column(GUID(), ForeignKey('teams.id'))
    team_id_away = Column(GUID(), ForeignKey('teams.id'))

    team_home = relationship("Team")
    team_away = relationship("Team")

    score_board = relationship("ScoreBoard", uselist=False, back_populates='match')

  
class ScoreBoard(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'score_board'

    score_home = Column(String)
    score_away = Column(String)

