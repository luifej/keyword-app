from sqlalchemy import Column, Integer, String, Float, DateTime, text
from .session import Base

class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True)
    volume = Column(Integer, nullable=True)
    cpc = Column(Float, nullable=True)
    difficulty = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
