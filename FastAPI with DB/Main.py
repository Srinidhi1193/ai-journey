from fastapi import FastAPI , Depends
from expense import Expense
from database import Session,engine
import expense_db
from sqlalchemy import func

app = FastAPI()

""" table loading with data """
expense_db.base.metadata.create_all(bind = engine)  

Expenses = [
    Expense(id=2, category="Food", amount=300),
    Expense(id=3, category="Skincare", amount=900),
    Expense(id=1, category="Food", amount=500),
    Expense(id=4, category="Electronics", amount=1200),
    Expense(id=5, category="Groceries", amount=1000)
]

def init_db():
    db = Session()
    try:
        count = db.query(expense_db.Expense).count()
        if count == 0:
            for expense in Expenses:
                db.add(expense_db.Expense(**expense.model_dump()))
            db.commit()
    finally:
        db.close()
init_db()

def db_get():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.post("/expense")
def add_expense(exp: Expense, db:Session = Depends(db_get)):
    db.add(expense_db.Expense(**exp.model_dump()))
    db.commit()
    return "Expense added successfully"

@app.get("/expenses")
def get_expenses(db: Session = Depends(db_get)):
    return db.query(expense_db.Expense).all()
    
@app.get("/totexp")
def get_expense(db:Session = Depends(db_get)):
    total = db.query(func.sum(expense_db.Expense.amount)).scalar()
    return {"total": total}
    

@app.get("/highexp")
def get_highest_expense(db:Session = Depends(db_get)):
    high = db.query(func.max(expense_db.Expense.amount)).scalar()
    return {"Highest expense": high}

@app.get("/expenses/{cat}")
def get_expense_by_category(cat: str, db:Session = Depends(db_get)):
    cat_list = db.query(expense_db.Expense).filter(expense_db.Expense.category == cat).all()
    return cat_list if cat_list else {"message": "No such category"}

@app.put("/expense/{id}")
def update_expense(id: int, exp: Expense, db:Session = Depends(db_get)):
    Expen = db.query(expense_db.Expense).filter(expense_db.Expense.id == id).first()
    if Expen:
        Expen.category = exp.category
        Expen.amount = exp.amount
        db.commit()
        return "Expense updated"    
    return "Expense with this id does not exist"

@app.delete("/expense/{id}")
def delete_expense(id: int, db:Session = Depends(db_get)):
    Expen = db.query(expense_db.Expense).filter(expense_db.Expense.id == id).first()
    if Expen:
        db.delete(Expen)
        db.commit()
        return "Expense deleted"
    return "Expense with this id does not exist"
    




