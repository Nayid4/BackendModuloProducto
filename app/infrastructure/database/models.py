from app import db
from sqlalchemy import CheckConstraint

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    min_stock = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('stock >= 0', name='check_stock_positive'),
        CheckConstraint('min_stock >= 0', name='check_min_stock_positive')
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'stock': self.stock,
            'min_stock': self.min_stock
        }
