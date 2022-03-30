from typing import Union

from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from crud.common import get_db
from crud.user_crud import get_user_by_email, add_user, update_user
from schemas.common_schemas import ErrorSchema
from schemas.user_schemas import UserIn, UserOut, UserUpdate

router = APIRouter()


@router.get('/get_user', response_model=Union[UserOut, ErrorSchema])
async def get_user_with_email(user_email: str, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to get user by its' email
        :param db_session: database session
        :param response:
        :param user_email: user email
    :return:
    """
    try:
        user = await get_user_by_email(db_session=db_session, user_email=user_email)
        return user
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.post('/add_new_user', response_model=Union[UserOut, ErrorSchema])
async def add_new_user(user: UserIn, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to create new user
        :param db_session: database session
        :param user: user information (email and first name)
        :param response:
    :return:
    """
    try:
        user = await add_user(db_session=db_session, user=user)
        return user
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')


@router.patch('/update_user_info', response_model=Union[UserOut, ErrorSchema])
async def update_user_info(user: UserUpdate, response: Response, db_session: Session = Depends(get_db)):
    """
    Endpoint to update user information (first name and last name)
        :param user: user information
        :param response:
        :param db_session: database session
    :return:
    """
    try:
        updated_user = await update_user(db_session=db_session, user_data=user)
        return updated_user
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')
