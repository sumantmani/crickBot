from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class User(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String)

class TelUser(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'telegram_users'

    name = Column(String(64), nullable=False)

