from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

base = declarative_base()

class Expense(base):

    __tablename__ = "expense"

    id = Column (Integer, primary_key=True, index= True)
    category = Column(String(50))
    amount = Column(Float)

