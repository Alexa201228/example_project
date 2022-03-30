from sqlalchemy import update
from sqlalchemy.orm import Session

from crud.common import catch_exception
from models import Question
from schemas.question_schemas import QuestionIn, QuestionUpdate


@catch_exception
async def get_question_by_id(db_session: Session, question_id: int) -> Question:
    """
    Method to get question by its' identifier
    :param db_session:
    :param question_id:
    :return:
    """
    question = db_session.query(Question).filter(Question.question_id == question_id).first()
    return question


@catch_exception
async def add_question_to_survey(db_session: Session, new_question: QuestionIn) -> Question:
    """
    Method to add new question to survey
    :param db_session:
    :param new_question:
    :return:
    """
    question = Question(text=new_question.question_text, survey_id=new_question.survey_id)
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)
    return question


@catch_exception
async def update_question(db_session: Session, question_data: QuestionUpdate) -> Question:
    """
    Method to update question info
    :param db_session:
    :param question_data:
    :return:
    """
    db_session.execute(update(Question)
                       .where(Question.question_id == question_data.question_id)
                       .values(text=question_data.new_text))
    db_session.commit()
    return await get_question_by_id(db_session=db_session, question_id=question_data.question_id)


@catch_exception
async def delete_question(db_session: Session, question_id: int):
    """
    Method to delete question from db
    :param db_session:
    :param question_id:
    :return:
    """
    db_session.delete(db_session.query(Question).filter(Question.question_id == question_id).first())
    db_session.commit()
