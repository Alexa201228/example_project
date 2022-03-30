from sqlalchemy import update
from sqlalchemy.orm import Session

from crud.common import catch_exception
from models import Survey
from schemas.survey_schemas import SurveyIn, SurveyUpdate


@catch_exception
async def get_survey_by_id(db_session: Session, survey_id: int) -> Survey:
    """
    Method to get survey by its' id
    :param db_session:
    :param survey_id:
    :return:
    """
    survey = db_session.query(Survey).filter(Survey.survey_id == survey_id).first()
    return survey


@catch_exception
async def add_survey(db_session: Session, new_survey: SurveyIn) -> Survey:
    """
    Method to add new survey with description
    :param db_session:
    :param new_survey:
    :return:
    """
    survey = Survey(description=new_survey.description)
    db_session.add(survey)
    db_session.commit()
    db_session.refresh(survey)
    return survey


@catch_exception
async def update_survey(db_session: Session, survey_info: SurveyUpdate) -> Survey:
    """
    Method to update survey description
    :param db_session: database session
    :param survey_info: survey information
    :return:
    """
    db_session.execute(update(Survey)
                       .where(Survey.survey_id == survey_info.survey_id)
                       .values(description=survey_info.new_description))
    db_session.commit()
    return await get_survey_by_id(db_session=db_session, survey_id=survey_info.survey_id)


async def delete_survey(db_session: Session, survey_id: int) -> None:
    """
    Method to delete survey by its' id
    :param db_session:
    :param survey_id:
    :return:
    """
    db_session.delete(db_session.query(Survey).filter(Survey.survey_id == survey_id).first())
    db_session.commit()
