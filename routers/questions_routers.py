from typing import Union

from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from crud.common import get_db
from crud.question_crud import get_question_by_id, add_question_to_survey, update_question, delete_question
from schemas.common_schemas import ErrorSchema
from schemas.question_schemas import QuestionOut, QuestionIn, QuestionUpdate

router = APIRouter()


@router.get('/get_question', response_model=Union[QuestionOut, ErrorSchema])
async def get_question(question_id: int, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to get question by its' id
    :param question_id:
    :param response:
    :param db_session:
    :return:
    """
    try:
        question = await get_question_by_id(db_session=db_session, question_id=question_id)
        return question
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.post('/add_question', response_model=Union[QuestionOut, ErrorSchema])
async def add_question(new_question: QuestionIn, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to add new question to survey
    :param new_question:
    :param response:
    :param db_session:
    :return:
    """
    try:
        question = await add_question_to_survey(db_session=db_session, new_question=new_question)
        return question
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.patch('/update_question', response_model=Union[QuestionOut, ErrorSchema])
async def update_survey_question(question: QuestionUpdate, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to update question text
    :param question:
    :param response:
    :param db_session:
    :return:
    """
    try:
        updated_question = await update_question(db_session=db_session, question_data=question)
        return updated_question
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.delete('/delete_question')
async def delete_survey_question(question_id: int, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to remove question from survey
    :param question_id:
    :param response:
    :param db_session:
    :return:
    """
    try:
        await delete_question(db_session=db_session, question_id=question_id)
        return {'question_deleted': True}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')
