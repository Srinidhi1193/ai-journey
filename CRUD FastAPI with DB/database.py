from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "mysql+mysqlconnector://root:Sri%231193@localhost:3306/product"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit = False, bind=engine)

try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print("Database connection failed:")
    print(e)