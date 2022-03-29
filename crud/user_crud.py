from sqlalchemy import update
from sqlalchemy.orm import Session

from crud.common import catch_exception
from models import User
from schemas.user_schemas import UserUpdate


@catch_exception
async def get_user_by_id(db_session: Session, user_id: int) -> User:
    """
    Method to get user by its' identifier
    :param db_session: database session
    :param user_id: user identifier
    :return:
    """
    user = db_session.query(User).filter(User.user_id == user_id).first()
    return user


@catch_exception
async def get_user_by_email(db_session: Session, user_email: str) -> User:
    """
    Method to retrieve user from db by its' email
    :param db_session: database session
    :param user_email: user email
    :return:
    """
    user = db_session.query(User).filter(User.email == user_email).first()
    return user


@catch_exception
async def add_user(db_session: Session, user_email: str) -> User:
    """
    Method to add new user to db
    :param db_session:
    :param user_email:
    :return:
    """
    new_user = User(email=user_email)
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user


@catch_exception
async def update_user(db_session: Session, user_data: UserUpdate) -> User:
    """
    Method to update user info (first name and last name)
    :param db_session:
    :param user_data:
    :return:
    """
    db_session.execute(update(User)
                       .where(User.user_id == UserUpdate.user_id)
                       .values(first_name=UserUpdate.first_name,
                               last_name=UserUpdate.last_name))
    db_session.commit()
    return await get_user_by_id(user_id=UserUpdate.user_id)