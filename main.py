# pip install fastapi - сам фреймворк (включает pydantic - парсинг и валидация данных
# и starlette - легковесный ASGI фреймворк, который позволяет создавать быстрые асинхронные приложения)
# ASGI - это клиент-серверный протокол взаимодействия, прослойка между web сервером и кодом, которая позволяет
# использовать асинхронный код для обработки пользовательских HTTP запросов
# pip install uvicorn - быстрый ASGI web сервер для запуска приложения
# pip install "pydantic[email]" -
# pip install passlib
# pip install bcrypt
# pip install python-jose

from fastapi import FastAPI
import uvicorn

from db.base import database
from endpoints import users, auth

app = FastAPI(title="Employment exchange")
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=9999, host="0.0.0.0", reload=True)
