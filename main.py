from fastapi import FastAPI
from app.models import customer, product, order, association
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import engine
from app.controllers import customer_orders

customer.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer_orders.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML page directly
@app.get("/")
async def read_html():
    return FileResponse("static/index.html")