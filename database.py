from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/edtech_db"

engine=create_engine(DATABASE_URL, echo=True,pool_pre_ping=True)
SessionLocal=sessionmaker(autocomit=False, autoflush=False, bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal
    try:
        yield db
        print("Connected to database")
    finally:
        db.close()

def test_connection():
    try:
        with engine.connect() as connection:
            print("Database connection successful!")
    except OperationalError as e:
        print("Databese connection failed!")
        print(e)

if __name__ =="__main__":
    test_connection()