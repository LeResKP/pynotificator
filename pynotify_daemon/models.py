from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    ForeignKey,
    Table,
    Boolean,
    create_engine,
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
)

from zope.sqlalchemy import ZopeTransactionExtension
from sqla_declarative import extended_declarative_base

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = extended_declarative_base(DBSession)
engine = create_engine('sqlite:///pynotify-daemon.db', echo=False)
DBSession.configure(bind=engine)
Base.metadata.bind = engine


class Notification(Base):
    __tablename__ = 'notification'

    idnotification = Column(
        Integer,
        nullable=False,
        autoincrement=True,
        primary_key=True)
    title = Column(
        String(255),
        nullable=False)
    msg = Column(
        Text,
        nullable=False)
    sent = Column(
        Boolean,
        nullable=False,
        default=False
    )
