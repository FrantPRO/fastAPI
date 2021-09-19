import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    hash_password: str
    is_company: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str
    is_company: bool = False

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        """
        Проверка соответствия пароля 2 паролю 1
        :param v: значение поля  password2 - которое проверяем
        :param values: все значения полученные от пользователя
        :param kwargs:
        :return: ошибка если не равны, иначе возвращаем пароля 2
        """
        if "password" in values and v != values["password"]:
            raise ValueError("Password don't match")
        return v

