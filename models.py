from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Boolean

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'tasks'
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(100))
    completed : Mapped[bool] = mapped_column(Boolean, default=False)