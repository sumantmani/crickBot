from sqlalchemy import Column, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class Admin(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'admins'

    name = Column(String(64), nullable=False)
    email = Column(String(24), unique=True, nullable=False)
    password_hash = Column(String)

