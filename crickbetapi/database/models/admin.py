from sqlalchemy import Column, String

from .metadata.common import Base
from .metadata.mixins import HasCreatedAt, HasUpdatedAt, HasUUIDID

class Admin(Base, HasUUIDID, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'admins'

    name = Column(String(64), nullable=False)
    fullname = Column(String(64), nullable=False)
    email = Column(String(24), unique=True, nullable=False)
    password_hash = Column(String)

'''
    def __repr__(self):
        return "<Admin(name={}, fullname={}, email_id={}, passwrod_hash={})>"
    .format(self.name, self.fullname, self.email_id, self.password_hash)

'''
