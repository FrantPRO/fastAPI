import sqlalchemy as sa
from db.base import metadata
import datetime

jobs = sa.Table(
    "jobs",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
    sa.Column("title", sa.String),
    sa.Column("description", sa.String),
    sa.Column("salary_from", sa.Integer),
    sa.Column("salary_to", sa.Integer),
    sa.Column("is_active", sa.Boolean),
    sa.Column("created_at", sa.DateTime, default=datetime.datetime.utcnow()),
    sa.Column("updated_at", sa.DateTime, default=datetime.datetime.utcnow()),
)
