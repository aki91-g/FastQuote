from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

user_related_quotes = Table(
    "user_favorites",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("quote_id", Integer, ForeignKey("quotes.id"), primary_key=True),
)

user_seen_quotes = Table(
    "user_seen_quotes",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("quote_id", Integer, ForeignKey("quotes.id"), primary_key=True),
)


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=True)

    author = relationship("authors", back_populates="quotes")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_year = Column(String, nullable=True)
    death_year = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    
    quotes = relationship("Quote", back_populates="author")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Integer, default=1)  # 1 for True, 0 for False

    favorite_quotes = relationship("Quote", secondary=user_related_quotes, back_populates="favorited_by")
    seen_quotes = relationship("Quote", secondary=user_related_quotes, back_populates="seen_by")