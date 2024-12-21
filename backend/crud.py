from sqlmodel import SQLModel

class CRUD:
    def __init__(self, model: SQLModel):
        self.model = model

    def create():
        pass

    def read(self, obj_id):
        pass

    def update(self, obj_id):
        pass

    def delete(self, obj_id):
        pass