from fastapi import FastAPI

from routers import user_routers, survey_routers, questions_routers, answer_routers
from configs import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user_routers.router, tags=['user endpoints'])
app.include_router(survey_routers.router, tags=['survey endpoints'])
app.include_router(questions_routers.router, tags=['question endpoints'])
app.include_router(answer_routers.router, tags=['answer endpoints'])
