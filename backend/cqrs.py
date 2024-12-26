from sqlmodel import SQLModel, select
from sqlalchemy.exc import NoResultFound

class crudOperations:
    async def create_obj(model: SQLModel, session, data):
        """
        Create a new entry in the database.
        Returns:
            The newly created object.
        """
        obj = model(**data)
        await session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def read_obj(model: SQLModel, session, obj_id):
        """
        Read an entry by its ID.
        Args:
            obj_id: The primary key of the object to retrieve.
        Returns:
            The object if found, or raises an exception if not.
        """
        query = select(model).where(model.id == obj_id)
        result = session.exec(query).scalar_one_or_none()
        if not result:
            raise NoResultFound(f"{model.__name__} with ID {obj_id} not found.")
        return result
    
    async def read_objs(model: SQLModel, session):
        """
        Return object entries.
        """
        statement = select(model)
        results = await session.exec(statement)
        items = results.scalars().all()
        return items


    async def update_obj(model: SQLModel, session, obj_id, data):
        """
        Update an existing entry in the database.
        Args:
            obj_id: The primary key of the object to update.
        Returns:
            The updated object.
        """
        obj = select(model).where(model.id == obj_id)
        for key, value in data.items():  # Update fields dynamically
            setattr(obj, key, value)
        session.commit()
        session.refresh(obj)
        return obj

    async def delete_obj(model: SQLModel, obj_id, session):
        """
        Delete an entry from the database.
        Args:
            obj_id: The primary key of the object to delete.
        Returns:
            A message indicating the object has been deleted.
        """
        obj = select(model).where(model.id == obj_id)
        session.delete(obj)
        session.commit()
        return {"message": f"{model.__name__} with ID {obj_id} has been deleted."}