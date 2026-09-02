from fastapi import FastAPI,Depends
from Product import Product
from database import session,engine
import Prod_model_db
from sqlalchemy.orm import Session

app = FastAPI()

Prod_model_db.base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "welcome to fastAPI"
greet()

products = [
    Product(id =1, name="book", quantity=5, price=40, description="to take notes"),
    Product(id =2, name="pen", quantity=2, price=10, description="to write"),
    Product(id =7, name="pencil", quantity=2, price=5, description="to write"),
    Product(id =9, name="bottle", quantity=1, price=90, description="to drink water"),
    Product(id =4, name="bag", quantity=1, price=150, description="to carry things")
]


def init_db():
    db = session()
    try:
        count = db.query(Prod_model_db.Product).count()
        if count == 0:
            for prod in products:
                db.add(Prod_model_db.Product(**prod.model_dump()))
        db.commit()
    finally:
        db.close()
init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    return db.query(Prod_model_db.Product).all()


@app.get("/product/{id}")
def get_product_by_id(id: int, db:Session = Depends(get_db)):
    prod = db.query(Prod_model_db.Product).filter(Prod_model_db.Product.id == id).first()
    return prod if prod else "Product does not exist"

@app.post("/product")
def create_product(product:Product, db:Session = Depends(get_db)):
    db.add(Prod_model_db.Product(**product.model_dump()))
    db.commit()
    return "Product Added successfully"

@app.put("/product/{id}")
def update_product(id: int, product:Product, db:Session = Depends(get_db)):
    avail = db.query(Prod_model_db.Product).filter(Prod_model_db.Product.id == id).first()
    if avail:
        avail.name = product.name
        avail.quantity = product.quantity
        avail.price = product.price
        avail.description = product.description
        db.commit()
        return "Product updated successfully"
    return "Product does not exist"

@app.delete("/product/{id}")
def delete_product(id: int, db:Session = Depends(get_db)):
    product = db.query(Prod_model_db.Product).filter(Prod_model_db.Product.id == id).first()
    if product:
        db.delete(product)
        db.commit()
        return "Product deleted successfully"
    return "Product does not exist"





