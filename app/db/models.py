from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import DateTime

from sqlalchemy.sql import func

from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)

    password = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )