from __future__ import annotations

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String)


class Survey(Base):

    __tablename__ = 'survey'

    survey_id = Column(Integer, primary_key=True, index=True)
