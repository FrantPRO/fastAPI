# Репозиторий - это паттерн, который представляет собой слой абстракции инкапсулирующий способ хранения данных
from databases import Database


class BaseRepository:

    def __init__(self, database: Database):
        self.database = database
