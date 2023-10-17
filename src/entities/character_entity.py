from src.entities.base_entity import BaseEntity, Base
from sqlalchemy.orm import Mapped, mapped_column


class CharacterEntity(Base, BaseEntity):
    __tablename__ = "characters"

    name: Mapped[str] = mapped_column(nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    mass: Mapped[int] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    skin_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
