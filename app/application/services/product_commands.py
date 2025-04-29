from app.infrastructure.database.models import ProductModel

class CreateProductCommand:
    def __init__(self, db):
        self.db = db

    def handle(self, data):
        new_product = ProductModel(
            name=data['name'],
            code=data['code'],
            stock=int(data['stock']),
            min_stock=int(data['min_stock'])
        )
        self.db.session.add(new_product)
        self.db.session.commit()
        return new_product.to_dict()