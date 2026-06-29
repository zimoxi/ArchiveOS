from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class ApprovalRecord(Base):
    __tablename__ = "approval_records"

    id = Column(Integer, primary_key=True)
    target_type = Column(String)  # borrow/download
    target_id = Column(Integer)
    status = Column(String, default="pending")
    approver_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
