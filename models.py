from __future__ import annotations

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class User(Base):
    """
    User model
    """

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String)


class Survey(Base):
    """
    Survey model
    """

    __tablename__ = 'survey'

    survey_id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

    questions = relationship('Question', backref='survey')


class Question(Base):
    """
    Question model
    """

    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    survey_id = Column(Integer, ForeignKey('survey.id', name='fk_question_survey'))

    answers = relationship('Answer')
    survey = relationship('Survey', backref=backref('questions', lazy='dynamic'))


class Answer(Base):
    """
    Answer model
    """
    __tablename__ = 'answer'

    answer_id = Column(Integer, primary_key=True, index=True)
    answer_text = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id', name='fk_answer_question'))

    question = relationship('Question', backref=backref('answers', lazy='dyncamic'))

