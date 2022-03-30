from sqlalchemy import update
from sqlalchemy.orm import Session

from crud.common import catch_exception
from models import Answer
from schemas.answer_schemas import AnswerIn, AnswerUpdate


@catch_exception
async def get_answer_by_id(db_session: Session, answer_id: int) -> Answer:
    """
    Method to get answer by id
    :param db_session:
    :param answer_id:
    :return:
    """
    answer = db_session.query(Answer).filter(Answer.answer_id == answer_id).first()
    return answer


@catch_exception
async def add_answer(db_session: Session, new_answer: AnswerIn) -> Answer:
    """
    Method to add new answer to question
    :param db_session:
    :param new_answer:
    :return:
    """
    answer = Answer(answer_text=new_answer.answer_text, question_id=new_answer.question_id)
    db_session.add(answer)
    db_session.commit()
    db_session.refresh(answer)
    return answer


@catch_exception
async def update_answer(db_session: Session, answer_data: AnswerUpdate) -> Answer:
    """
    Method to update answer text
    :param db_session:
    :param answer_data:
    :return:
    """
    db_session.execute(update(Answer)
                       .where(Answer.answer_id == answer_data.answer_id)
                       .values(answer_text=answer_data.new_answer_text))
    db_session.commit()
    return await get_answer_by_id(db_session=db_session, answer_id=answer_data.answer_id)


@catch_exception
async def delete_answer(db_session: Session, answer_id: int) -> None:
    """
    Method to delete answer from question
    :param db_session:
    :param answer_id:
    :return:
    """
    db_session.delete(db_session.query(Answer).filter(Answer.answer_id == answer_id).first())
    db_session.commit()
