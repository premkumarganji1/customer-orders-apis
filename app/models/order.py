from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from app.models.association import order_product_association

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer")
    products = relationship(
        "Product",
        secondary=order_product_association,
        back_populates="orders"
    )
