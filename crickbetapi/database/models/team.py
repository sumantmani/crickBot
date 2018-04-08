from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .metadata.common import Base
from .metadata.mixins import GUID, HasCreatedAt, HasUpdatedAt, HasUUIDID

class Team(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'teams'

    name = Column(String(64), nullable=False)
    pretty_name = Column(String(64), nullable=False)

    code = Column(String(4), nullable=False)
    
    players = relationship('Player', back_populates='team')

