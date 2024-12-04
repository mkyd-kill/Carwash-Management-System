from sqlmodel import create_engine, SQLModel

database_file_name = "carManagement.db"
database_file_url = f"sqlite:///{database_file_name}"

connect_args = {
    "check_same_thread": False
}
engine = create_engine(database_file_url, connect_args=connect_args)

# creating the database with tables
def create_database():
    SQLModel.metadata.create_all(engine)