from sqlmodel import SQLModel, select
from sqlalchemy.exc import NoResultFound

class CRUD:
    def __init__(self, model: SQLModel, session, data, engine):
        """
        Initializes the CRUD object.
        Args:
            model (SQLModel): The SQLModel class for the target table.
            session (Session): The SQLAlchemy session object.
            data (dict): The data to be used for CRUD operations.
            engine: The SQLAlchemy engine object.
        """
        self.model = model
        self.session = session
        self.data = data
        self.engine = engine

    def create(self):
        """
        Create a new entry in the database.
        Returns:
            The newly created object.
        """
        obj = self.model(**self.data)  # Create a model instance with the provided data
        self.session.add(obj)  # Add the instance to the session
        self.session.commit()  # Commit the transaction
        self.session.refresh(obj)  # Refresh the instance with updated data (e.g., primary key)
        return obj

    def read(self, obj_id):
        """
        Read an entry by its ID.
        Args:
            obj_id: The primary key of the object to retrieve.
        Returns:
            The object if found, or raises an exception if not.
        """
        query = select(self.model).where(self.model.id == obj_id)
        result = self.session.execute(query).scalar_one_or_none()
        if not result:
            raise NoResultFound(f"{self.model.__name__} with ID {obj_id} not found.")
        return result

    def update(self, obj_id):
        """
        Update an existing entry in the database.
        Args:
            obj_id: The primary key of the object to update.
        Returns:
            The updated object.
        """
        obj = self.read(obj_id)  # Fetch the existing object
        for key, value in self.data.items():  # Update fields dynamically
            setattr(obj, key, value)
        self.session.commit()  # Commit the changes
        self.session.refresh(obj)  # Refresh the instance
        return obj

    def delete(self, obj_id):
        """
        Delete an entry from the database.
        Args:
            obj_id: The primary key of the object to delete.
        Returns:
            A message indicating the object has been deleted.
        """
        obj = self.read(obj_id)  # Fetch the existing object
        self.session.delete(obj)  # Mark it for deletion
        self.session.commit()  # Commit the changes
        return {"message": f"{self.model.__name__} with ID {obj_id} has been deleted."}
