from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class BorrowRecord(Base):
    __tablename__ = "borrow_records"

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer)
    user_id = Column(Integer)
    status = Column(String, default="pending")  # pending/approved/rejected/returned
    created_at = Column(DateTime, default=datetime.utcnow)
    returned_at = Column(DateTime, nullable=True)
