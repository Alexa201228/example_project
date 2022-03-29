from typing import Union

from fastapi import APIRouter, Response, status

from crud.user_crud import get_user_by_email
from schemas.common_schemas import ErrorSchema
from schemas.user_schemas import UserOut

router = APIRouter()


@router.get('/get_user', response_model=Union[UserOut, ErrorSchema])
async def get_user_with_email(user_email: str, response: Response):
    """
    Endpoint to get user by its' email
    :param response:
    :param user_email:
    :return:
    """
    try:
        user = await get_user_by_email(user_email=user_email)
        return user
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorSchema(error=f'Error type: {type(e).__name__}. Error message: {e}')



