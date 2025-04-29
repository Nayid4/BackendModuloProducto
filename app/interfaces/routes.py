from flask import Blueprint, request, jsonify
from http import HTTPStatus
from app import db
from app.application.services.product_commands import CreateProductCommand
from app.application.services.product_queries import GetProductsQuery, GetAlertsQuery

bp = Blueprint('routes', __name__)

@bp.route('/products', methods=['GET'])
def get_products():
    result = GetProductsQuery().handle()
    return jsonify(result), HTTPStatus.OK

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    required = {'name', 'code', 'stock', 'min_stock'}
    if not data or not required.issubset(data):
        return jsonify({'error': 'Missing fields'}), HTTPStatus.BAD_REQUEST
    try:
        result = CreateProductCommand(db).handle(data)
        return jsonify(result), HTTPStatus.CREATED
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

@bp.route('/alerts', methods=['GET'])
def get_alerts():
    result = GetAlertsQuery().handle()
    return jsonify(result), HTTPStatus.OK