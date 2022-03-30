from pydantic import BaseModel


class AnswerBase(BaseModel):
    answer_id: int


class AnswerIn(BaseModel):
    answer_text: str
    question_id: int


class AnswerOut(AnswerBase):
    answer_text: str

    class Config:
        orm_mode = True


class AnswerUpdate(AnswerBase):
    new_answer_text: str
