
from pydantic import BaseModel


class SurveyBase(BaseModel):
    survey_id: int


class SurveyIn(BaseModel):
    description: str


class SurveyOut(SurveyBase):
    description: str

    class Config:
        orm_mode = True


class SurveyUpdate(SurveyBase):
    new_description: str
