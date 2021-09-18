import sqlalchemy as sa
from db.base import metadata
import datetime

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("email", sa.String, primary_key=True, unique=True),
    sa.Column("name", sa.String),
    sa.Column("hash_password", sa.String),
    sa.Column("is_company", sa.Boolean),
    sa.Column("created_at", sa.DateTime, default=datetime.datetime.utcnow()),
    sa.Column("updated_at", sa.DateTime, default=datetime.datetime.utcnow()),
)
