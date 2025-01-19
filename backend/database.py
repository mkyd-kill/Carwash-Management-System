from sqlmodel import SQLModel, create_engine

database_file_name = "orm.db"
database_file_url = f"sqlite:///{database_file_name}"

connect_args = {
    "check_same_thread": False
}

engine = create_engine(database_file_url, connect_args=connect_args, echo=False)

# creating the database with tables
def create_database():
    SQLModel.metadata.create_all(engine)