from sqlalchemy import Column, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class Team(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'teams'

    name = Column(String)

