from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    orders = relationship("Order", back_populates="branch")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    customer_name = Column(String, nullable=False)
    order_time = Column(DateTime, default=datetime.now)
    collect_flag = Column(String, default="")
    drivedat_no = Column(Integer, default=0)
    branch = relationship("Branch", back_populates="orders")