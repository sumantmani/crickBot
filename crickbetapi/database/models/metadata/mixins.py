import uuid
import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID


class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)


class HasUUIDID(object):
    id = Column(GUID(), primary_key=True, default=uuid.uuid4)


class HasCreatedAt(object):
    created_at = Column(DateTime(), server_default=func.now())


class HasUpdatedAt(object):
    updated_at = Column(
        DateTime(),
        server_default=func.now(),
        onupdate=func.now())

    def touch(self):
        self.updated_at = func.now()

