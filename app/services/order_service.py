from fastapi import HTTPException
from ..models.order import Order
from ..models.product import Product
from ..models.customer import Customer


def create_order_service(db, order_data):
    customer = db.query(Customer).filter(Customer.id == order_data.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    products = db.query(Product).filter(Product.id.in_(order_data.product_ids)).all()
    if len(products) != len(order_data.product_ids):
        raise HTTPException(status_code=404, detail="One or more products not found")

    new_order = Order(customer_id=order_data.customer_id)
    new_order.products = products
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def get_order_service(db, order_id):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    total_cost = sum(product.price for product in order.products)

    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "created_at": order.created_at,
        "products": order.products,
        "total_cost": total_cost
    }
