from typing import Union

from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from crud.common import get_db
from crud.survey_crud import get_survey_by_id, add_survey, update_survey, delete_survey
from schemas.common_schemas import ErrorSchema
from schemas.survey_schemas import SurveyOut, SurveyIn, SurveyUpdate

router = APIRouter()


@router.get('/get_survey', response_model=Union[SurveyOut, ErrorSchema])
async def get_survey(survey_id: int, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to get survey by id
        :param survey_id:
        :param response:
        :param db_session:
    :return:
    """
    try:
        survey = await get_survey_by_id(db_session=db_session, survey_id=survey_id)
        return survey
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.post('/add_survey', response_model=Union[SurveyOut, ErrorSchema])
async def add_new_survey(new_survey: SurveyIn, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to add new survey
        :param new_survey:
        :param response:
        :param db_session:
    :return:
    """
    try:
        survey = await add_survey(db_session=db_session, new_survey=new_survey)
        return survey
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.patch('/update_survey', response_model=Union[SurveyOut, ErrorSchema])
async def update_survey_in_db(update_info: SurveyUpdate, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to update survey description
        :param update_info:
        :param response:
        :param db_session:
    :return:
    """
    try:
        updated_survey = await update_survey(db_session=db_session, survey_info=update_info)
        return updated_survey
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.delete('/delete_survey')
async def delete_existing_survey(survey_id: int, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to delete existing survey
    :param survey_id:
    :param response:
    :param db_session:
    :return:
    """
    try:
        await delete_survey(db_session=db_session, survey_id=survey_id)
        return {'survey deleted': True}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')
