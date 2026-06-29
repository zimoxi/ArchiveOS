from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    target = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
