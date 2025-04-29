from app.infrastructure.database.models import ProductModel

class DbContext:
    def __init__(self, db):
        self.db = db