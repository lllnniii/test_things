from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
import config

engine = create_engine(
    url=config.SQLALCHEMY_URL,
    echo=config.SQLALCHEMY_ECHO
)


class Base(DeclarativeBase):
    pass


class SpaceObj(Base):
    __tablename__ = 'space_objects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    x: Mapped[int]
    y: Mapped[int]
