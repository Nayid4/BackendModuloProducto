from app.infrastructure.database.db_context import DbContext
from app.infrastructure.database.models import ProductModel

class UnitOfWork:
    def __init__(self, db):
        self.context = DbContext(db)
        self.db = db

    def commit(self):
        self.db.session.commit()

    def rollback(self):
        self.db.session.rollback()