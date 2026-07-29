from sqlalchemy import String, Text, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.db.database import Base


class Page(Base):
    __tablename__ = "pages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    url: Mapped[str] = mapped_column(String(2048), unique=True, nullable=False)

    domain: Mapped[str] = mapped_column(String(255))

    title: Mapped[str] = mapped_column(String(500))

    description: Mapped[str] = mapped_column(Text)

    html: Mapped[str] = mapped_column(Text)

    text: Mapped[str] = mapped_column(Text)

    language: Mapped[str] = mapped_column(String(20))

    status_code: Mapped[int] = mapped_column(Integer)

    content_hash: Mapped[str] = mapped_column(String(64))

    crawl_depth: Mapped[int] = mapped_column(default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    last_crawled: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )