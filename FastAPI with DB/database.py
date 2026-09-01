from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "mysql+mysqlconnector://root:Sri%231193@localhost:3306/expense"
engine = create_engine(db_url)
Session = sessionmaker(autoflush = False, autocommit = False, bind = engine)