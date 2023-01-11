from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import engine

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)


class QueueStatus(Base):
    __tablename__ = 'queuestatus'

    id = Column(Integer, primary_key=True)
    current_status = Column(Integer, default=0)


class Queue(Base):
    __tablename__ = 'queue'

    id = Column(Integer, primary_key=True)
    key = Column(Integer)
