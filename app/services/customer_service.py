from app.models.customer import Customer
from sqlalchemy.orm import Session

def create_customer_service(db, customer):
    db_customer = Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers_service(db: Session):
    return db.query(Customer).all()
