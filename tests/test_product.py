import unittest

from flask import Flask, json

from apie.products import app


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_base_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        product = {
            "id": 1,
            "product_name": "car",
            "price": "$500.00",
            "quantity": 600,
            "category": "Electronics"
        }

        result = self.client.post('/api/v2/resources/product/',
                                  content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_get_all_products(self):
        result = self.client.get('/api/v2/resources/products/all')
        self.assertEqual(result.status_code, 200)

    def test_add_single_product(self):
        product = {
            "id": 1,
            "product_name": "car",
            "price": "$500.00",
            "quantity": 600,
            "category": "Electronics"
        }

        result = self.client.post('/api/v2/resources/product/', content_type='application/json',
                                  data=json.dumps(product)
                                  )

        self.assertEqual(result.status_code, 201)

    def test_unavailable_fetch(self):
        result = self.client.get('/api/v2/resources/products/')
        self.assertEqual(result.status_code, 404)

    def test_product_updated(self):
        product = {
            "product_name": "car",
            "price": "$500.00",
            "quantity": 600,
            "category": "Electronics"
        }
        result = self.client.put('/api/v2/resources/product/',
                                 content_type='application/json',
                                 data=json.dumps(product)
                                 )

        self.assertEqual(result.status_code, 405)
        self.assertIsNotNone(result)

    def test_invalid_update(self):
        product_list = []
        product = {
            "id": 1,
            "product_name": "car",
            "price": "$500.00",
            "quantity": 600,
            "category": "Electronics"
        }

        result = self.client.post('/api/v2/resources/product/',
                                  content_type='application/json',
                                  data=json.dumps(product)
                                  )

        product_list.append(product)
        self.assertEqual(result.status_code, 201)

        update = {
            "product_name": "fridge",
            "price": "$500.00",
            "quantity": 600,
            "category": "Electronics"
        }

        product = [product for product in product_list]
        product[0]['product_name'] = update['product_name']
        dict_name = {'product_name': product[0]['product_name']}
        result = self.client.put('/api/v2/resources/product/2', content_type='application/json',
                                 data=json.dumps(dict_name))

        self.assertEqual(result.status_code, 400)

    def test_entry_deleted(self):
        delete_list = []
        delete = {
            "id": 1,
            "product_name": "car",
            "price": "$5000.00",
            "quantity": 600,
            "category": "Electronics"
        }

        result = self.client.delete('/api/v2/resources/product/',
                                    content_type='application/json',
                                    data=json.dumps(delete)
                                    )

        delete_list.append(delete)
        self.assertEqual(result.status_code, 405)

    def test_add_product_with_empty_id(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="", product_name="car", price="$5000.00", quantity="600",
                 category="Electronics")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_product_with_empty_product_name(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", product_name="", price="$5000.00", quantity="600",
                 category="Electronics")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_product_with_empty_price(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", product_name="car", price="", quantity="600",
                 category="Electronics")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_product_with_empty_quantity(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", product_name="car", price="$5000.00", quantity="",
                 category="Electronics")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_product_with_empty_category(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", product_name="car", price="$5000.00", quantity="600",
                 category="")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_product_with_invalid_keys(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", product_name="car", price="$5000.00", quantity="600",
                 category="Electronics")), content_type='application/json')


    

    def test_add_sale(self):

        sale = {
            "id": 1,
            "sales_name": "wine",
            "price": "$200.00",
            "quantity": 1000,
            "category": "food and Beverages",
            "total": "$20000"
        }

        result = self.client.post('/api/v2/resources/order/',
                                  content_type='application/json',
                                  data=json.dumps(sale)
                                  )

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)

    def test_get_all_sales(self):
        result = self.client.get('/api/v2/resources/sale/all')
        self.assertEqual(result.status_code, 404)

    def test_add_single_sale(self):
        sale = {
            "id": 1,
            "sales_name": "wine",
            "price": "$200.00",
            "quantity": 1000,
            "category": "food and Beverages",
            "total": "$20000"
        }

        result = self.client.post('/api/v2/resources/sale/', content_type='application/json',
                                  data=json.dumps(sale)
                                  )

        self.assertEqual(result.status_code, 201)

    def test_sales_order_with_invalid_keys(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", sales_name="wine", price="$20.00", quantity="100",
                category="food and beverages", total="10000")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_sales_order_with_empty_id(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="", sales_name="wine", price="$20.00", quantity="100",
                 category="food and beverages", total="10000")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_sales_order_with_empty_name(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="2", sales_name="", price="$20.00", quantity="100",
                 category="food and beverages", total="10000")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_sales_order_with_empty_price(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", sales_name="wine", price="", quantity="100",
                 category="food and beverages", total="10000")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_sales_order_with_empty_quantity(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", sales_name="wine", price="$20.00", quantity="",
                 category="food and beverages", total="10000")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_sales_order_with_empty_category(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", sales_name="wine", price="$20.00", quantity="100",
                 category="", total="10000")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)

    def test_add_sales_order_with_empty_total(self):

        result = self.client.post("/api/v1/orders", data=json.dumps(
            dict(id="1", sales_name="wine", price="$20.00", quantity="100",
                 category="food and beverages", total="")), content_type='application/json')

        reply = json.loads(result.data)
        self.assertEqual(result.status_code, 404)
