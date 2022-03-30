
from pydantic import BaseModel


class QuestionBase(BaseModel):
    question_id: int


class QuestionIn(BaseModel):
    question_text: str
    survey_id: int


class QuestionUpdate(QuestionBase):
    new_text: str


class QuestionOut(QuestionBase):
    text: str

    class Config:
        orm_mode = True
