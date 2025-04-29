import unittest
from app import create_app, db
from app.infrastructure.database.models import ProductModel


class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def test_create_product(self):
        response = self.client.post('/products', json={
            'name': 'Laptop',
            'code': 'LP1001',
            'stock': 5,
            'min_stock': 10
        })
        self.assertEqual(response.status_code, 201)

    def test_create_product_missing_fields(self):
        response = self.client.post('/products', json={
            'name': 'Monitor',
            'stock': 10
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_create_product_duplicate_code(self):
        self.client.post('/products', json={
            'name': 'Teclado',
            'code': 'TC1001',
            'stock': 10,
            'min_stock': 5
        })
        response = self.client.post('/products', json={
            'name': 'Otro Teclado',
            'code': 'TC1001',  # mismo código
            'stock': 8,
            'min_stock': 4
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_get_products(self):
        self.client.post('/products', json={
            'name': 'Mouse',
            'code': 'MS1001',
            'stock': 20,
            'min_stock': 5
        })
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

    def test_get_products_empty(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_alerts(self):
        self.client.post('/products', json={
            'name': 'Teclado',
            'code': 'TC1001',
            'stock': 3,
            'min_stock': 5
        })
        response = self.client.get('/products/alerts')
        self.assertEqual(response.status_code, 200)
        alerts = response.get_json()
        self.assertEqual(len(alerts), 1)

    def test_alerts_no_alerts(self):
        self.client.post('/products', json={
            'name': 'Monitor',
            'code': 'MN1002',
            'stock': 10,
            'min_stock': 5
        })
        response = self.client.get('/products/alerts')
        self.assertEqual(response.status_code, 200)
        alerts = response.get_json()
        self.assertEqual(len(alerts), 0)


if __name__ == '__main__':
    unittest.main()
