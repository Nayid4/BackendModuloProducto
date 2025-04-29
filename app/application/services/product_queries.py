from app.infrastructure.database.models import ProductModel

class GetProductsQuery:
    def handle(self):
        return [p.to_dict() for p in ProductModel.query.all()]

class GetAlertsQuery:
    def handle(self):
        return [p.to_dict() for p in ProductModel.query.filter(ProductModel.stock < ProductModel.min_stock).all()]
