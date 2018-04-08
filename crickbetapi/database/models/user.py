from sqlalchemy import Column, Integer, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class User(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String)

