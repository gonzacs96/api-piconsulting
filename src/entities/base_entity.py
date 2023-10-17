from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class BaseEntity:
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
