from app.models.product import Product
from sqlalchemy.orm import Session

def create_product_service(db, product):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products_service(db: Session):
    return db.query(Product).all()
