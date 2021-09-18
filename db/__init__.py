from db.users import users
from db.jobs import jobs
from db.base import metadata, engine

metadata.create_all(bind=engine)
