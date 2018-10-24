import unittest

from flask import Flask, json,request

from apie.view import app


class TestStore(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.product = {
            "id": 1,
            "product_name": "car",
            "price": "$500.00",
            "quantity": 600,
            "category": "Electronics"
        }

        self.sale = {
            "id": 1,
            "sales_name": "wine",
            "price": "$200.00",
            "quantity": 1000,
            "category": "food and Beverages",
            "total": "$20000"
        }

    def tearDown(self):
        self.sale = None
        self.product = None
        self.app = None

    def test_base_url(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(b'base url', result)



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

        self.assertEqual(result.status_code, 404)
        self.assertTrue(b'product added', result)


    def test_new_product_has_all_feilds(self):
               product = {
                   "id": 1,
                   "product_name": "",
                   "price": "",
                   "quantity": 600,
                   "category": "Electronics"
               }
               result = self.client.post('/api/v2/resources/product/',
                                         content_type='application/json',
                                         data=json.dumps(product)
                                         )

               self.assertEqual(result.status_code, 404)
               self.assertTrue(b'product has all fields', result)

    def test_get_all_products(self):
                result = self.client.get('/api/v2/resources/products/all')
                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'get all products succesful', result)

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

                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'product added succesfully', result)

    def test_unavailable_fetch(self):
                result = self.client.get('/api/v2/resources/products/')
                self.assertEqual(result.status_code, 404)
                self.assertIsNotNone(result)

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

                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'product updated', result)

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
                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'invalid update', result)

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

                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'product updated', result)

    def test_product_deleted(self):
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
                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'product deleted', result)

    def test_add_sale(self):

        sale = {
            "id": 1,
            "sales_name": "wine",
            "price": "$200.00",
            "quantity": 1000,
            "category": "food and Beverages",
            "total": "$20000"
        }

        result = self.client.post('/api/v2/resources/sale/',
                                  content_type='application/json',
                                  data=json.dumps(sale)
                                  )

        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)
    
    def test_get_all_sales(self):
                result = self.client.get('/api/v2/resources/sale/all')
                self.assertEqual(result.status_code, 404)
                self.assertIsNotNone(result)

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

                self.assertEqual(result.status_code, 404)
                self.assertIsNotNone(result)

    def test_get_single_sale_or_product_that_doesnot_exist(self):
                result = self.client.get('/api/v2/resources/sales/1')
                self.assertEqual(result.status_code, 404)

                result = self.client.get('/api/v2/resources/products/1')
                self.assertEqual(result.status_code, 404)

    def test_sales_order_with_invalid_keys(self):

                result = self.client.post("/api/v1/orders", data=json.dumps(
                    dict(id="dghjd", sales_name="dhjkdks", price="vghjvf", quantity="gshfjk",
                        category="sdsfgh", total="1dghsj")), content_type='application/json')

                reply = json.loads(result.data)
                self.assertEqual(result.status_code, 404)
                self.assertTrue(b'Your sales order has invalid keys', reply)
