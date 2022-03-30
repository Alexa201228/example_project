# Survey service

Сервис для создания и прохождения опросов

Эндпоинты:
####Пользователь
- /get_user - находим пользователя по email
- /add_new_user - добавить пользователя с email и именем (обязательные поля)
- /update_user_info - обновление информации о пользователе (имя, фамилия)
####Опрос
- /get_survey - получение опроса по его id
- /add_survey - добавление опроса с его описанием
- /update_survey - обновление описания опроса
- /delete_survey - удаление опроса по id
####Вопрос в опросе
- /get_question - получение вопроса по id
- /add_question - добавление нового вопроса к опросу
- /update_question - обновление текста вопроса
- /delete_question - удаление вопроса по id 
####Ответ на вопрос
- /get_answer - получение ответа по id
- /add_answer - добавление нового ответа к вопросу
- /update_answer - обновление текста ответа
- /delete_answer - удаление ответа по id

Документация к API доступна через /docs (используется Swagger)

Использованные технологии:
- FastAPI
- SqlAlchemy
- Alembic
- Docker
- Pydantic
