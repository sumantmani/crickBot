from sqlalchemy import Column, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class Player(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'players'

    name = Column(String)
    position = Column(String)

    team_id = Column(String)

