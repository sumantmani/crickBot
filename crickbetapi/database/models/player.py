from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .metadata.common import Base
from .metadata.mixins import GUID, HasCreatedAt, HasUpdatedAt, HasUUIDID

class Player(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'players'

    name = Column(String)

    team_id = Column(GUID(), ForeignKey('teams.id'))

    team = relationship('Team', back_populates='players')


