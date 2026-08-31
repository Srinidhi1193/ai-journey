from fastapi import FastAPI
from product import Product

app = FastAPI()

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

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for prod in products:
        if prod.id == id:
            return prod
    return "Product does not exist"

@app.post("/product")
def create_product(product:Product):
    products.append(product)
    return "Product Added successfully"

@app.put("/product/{id}")
def update_product(id: int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
    return "Product does not exist"

@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"
    return "Product does not exist"





