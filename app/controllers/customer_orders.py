from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.customer import CustomerCreate, CustomerOut
from app.services.customer_service import create_customer_service, get_customers_service
from app.schemas.product import ProductCreate, ProductOut
from app.services.product_service import create_product_service, get_products_service
from app.schemas.order import OrderCreate, OrderOut
from app.services.order_service import create_order_service, get_order_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer_service(db, customer)


@router.get("/customers/", response_model=list[CustomerOut])
def get_customers(db: Session = Depends(get_db)):
    return get_customers_service(db)


@router.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product_service(db, product)


@router.get("/products/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return get_products_service(db)


@router.post("/orders/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order_service(db, order)


@router.get("/orders/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return get_order_service(db, order_id)
