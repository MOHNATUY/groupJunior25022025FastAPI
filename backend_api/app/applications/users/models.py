import uuid

from applications.database.base_models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from datetime import datetime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())
    uuid_data: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
