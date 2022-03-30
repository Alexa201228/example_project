from sqlalchemy import update
from sqlalchemy.orm import Session

from crud.common import catch_exception
from models import User
from schemas.user_schemas import UserUpdate, UserIn


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
async def add_user(db_session: Session, user: UserIn) -> User:
    """
    Method to add new user to db
    :param user:
    :param db_session:
    :return:
    """
    new_user = User(email=user.email, first_name=user.first_name)
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user


@catch_exception
async def update_user(db_session: Session, user_data: UserUpdate) -> User:
    """
    Method to update user info (first name and last name)
    :param db_session:
    :param user_data: new user information
    :return:
    """
    db_session.execute(update(User)
                       .where(User.user_id == user_data.user_id)
                       .values(first_name=user_data.first_name,
                               last_name=user_data.last_name))
    db_session.commit()
    return await get_user_by_id(user_id=user_data.user_id)
