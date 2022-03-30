from typing import Union

from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from crud.answer_crud import get_answer_by_id, add_answer, update_answer, delete_answer
from crud.common import get_db
from schemas.answer_schemas import AnswerOut, AnswerIn, AnswerUpdate
from schemas.common_schemas import ErrorSchema

router = APIRouter()


@router.get('/get_answer', response_model=Union[AnswerOut, ErrorSchema])
async def get_answer(answer_id: int, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to get answer by id
    :param answer_id:
    :param response:
    :param db_session:
    :return:
    """
    try:
        answer = await get_answer_by_id(db_session=db_session, answer_id=answer_id)
        return answer
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.post('/add_answer', response_model=Union[AnswerOut, ErrorSchema])
async def add_new_answer(new_answer: AnswerIn, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to add new answer to question
    :param new_answer:
    :param response:
    :param db_session:
    :return:
    """
    try:
        answer = await add_answer(db_session=db_session, new_answer=new_answer)
        return answer
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.patch('/update_answer', response_model=Union[AnswerOut, ErrorSchema])
async def update_answer_info(answer_info: AnswerUpdate, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to update answer text
    :param answer_info:
    :param response:
    :param db_session:
    :return:
    """
    try:
        updated_answer = await update_answer(db_session=db_session, answer_data=answer_info)
        return updated_answer
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.delete('/delete_answer')
async def delete_answer_from_question(answer_id: int, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to delete answer from question
    :param answer_id:
    :param response:
    :param db_session:
    :return:
    """
    try:
        await delete_answer(db_session=db_session, answer_id=answer_id)
        return {'answer deleted': True}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')
