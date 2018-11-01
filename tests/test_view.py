import unittest

from flask import Flask, json, request, Response

from apie.view import app

from apie.models.model import Product, Sale, User


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.product = {
            "id": 1,
            "product_name": "car",
            "price": 500.00,
            "quantity": 600,
            "category": "Electronics"
        }

        self.sale = {
            "id": 1,
            "sale_name": "wine",
            "price": 200.00,
            "quantity": 1000,
            "category": "food and Beverages",
            "total": "$20000"
        }

    def test_base_url(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(b'base url', result)

    def test_add_product_successfully(self):
        products = []
        product = {
            "id": 1,
            "product_name": "car",
            "price": 500.00,
            "quantity": 600,
            "category": "Electronics"
        }

        products.append(product)
        result = self.client.post('/api/v1/product/',
                                  content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 201)
        data = json.loads(result.data.decode())
        self.assertEqual(data['message'], "succesfully added")
        self.client.delete('/api/v1/product/1')

    def test_fetch_all_products(self):
        result = self.client.get('/api/v1/products/all',
                                 content_type='application/json')

        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data.decode())
        self.client.delete('/api/v1/products/all')



    def test_unavailable_fetch(self):
        result = self.client.get('/api/v1/products/')
        self.assertEqual(result.status_code, 404)

    def test_add_sale_successfully(self):
        sales = []
        Sale = {
            "id": 1,
            "sale_name": "car",
            "price": 20000,
            "quantity": 600,
            "category": "Electronics",
            "total":35544
        }

        data = sales.append(Sale)
        result = self.client.post('/api/v1/sale/',
                                  content_type='application/json',
                                  data=json.dumps(Sale)
                                  )

        self.assertEqual(result.status_code, 201)
        data = json.loads(result.data.decode())
        self.assertEqual(data['message'], "succesfully added")
        self.client.delete('/api/v1/sale/1')

    def test_fetch_all_sales(self):
        result = self.client.get('/api/v1/sales/all',
                                 content_type='application/json')

        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data.decode())
        self.client.delete('/api/v1/sale/all')

    