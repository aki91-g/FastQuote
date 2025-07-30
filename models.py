from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

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




