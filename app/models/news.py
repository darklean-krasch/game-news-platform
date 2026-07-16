from sqlalchemy import (
    String,
    Text,
    DateTime
)

from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.db.base import Base


class News(Base):

    __tablename__ = "news"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    title: Mapped[str] = mapped_column(
        String(255)
    )


    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


    url: Mapped[str] = mapped_column(
        String(500)
    )

