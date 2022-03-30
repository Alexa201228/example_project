import logging
from functools import wraps

from fastapi import Depends
from sqlalchemy.orm import Session

from configs import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def catch_exception(func):
    @wraps(func)
    async def wrapper(db_session: Session, *args, **kwargs):
        try:
            result = await func(db_session=db_session, *args, **kwargs)
            return result
        except Exception as e:
            logging.error(str(e))
            db_session.rollback()
            raise e

    return wrapper
