# pip install sqlalchemy - подключение в БД, используем только core так как библиотека не поддерживает асинхронность,
#    поэтому будем только генерировать запросы
# pip install databases - для асинхронной работы с БД
# pip install "databases[postgresql]" - обертка для работы с PostgreSQL
# pip install psycopg2-binary - адаптер для подключения к PostgreSQL

from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_URL

# создаем подключение
database = Database(DATABASE_URL)

# объект для создания таблиц
metadata = MetaData()

# только для синхронных запросов к базе
engine = create_engine(DATABASE_URL, )
