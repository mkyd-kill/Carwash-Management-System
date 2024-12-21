from sqlmodel import SQLModel, create_engine
from .models import Clients, Staff, Transaction, Report

database_file_name = "carManagement.db"
database_file_url = f"sqlite:///{database_file_name}"

connect_args = {
    "check_same_thread": False
}

engine = create_engine(database_file_url, connect_args=connect_args, echo=True)

# creating the database with tables
def create_database():
    print("CREATING DATABASE............")
    SQLModel.metadata.create_all(engine)