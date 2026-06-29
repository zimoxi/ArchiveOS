from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class Archive(Base):
    __tablename__ = "archives"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, default="")
    category = Column(String, default="")
    file_path = Column(String)
    created_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
