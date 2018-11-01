from flask import json, request, abort,jsonify

users = []

class Product:
    def __init__(self):
        self.products = []

    def add_product(self):
        self.products.append({
          'id':len(self.products) +1,
          'product_name': request.json['product_name'],
          'price': request.json['price'],
          'quantity': request.json['quantity'],
          'category': request.json['category']  
        })

    def get_all_products(self):
        return self.products

    def get_a_single_product_by_id(self, id):
        product=[product for product in self.products if product['id']==id]
        if len(product)==0:
            abort(404)
            return product[0]


class Sale:
    def __init__(self):
        self.sales = []

    def add_order(self):
        self.sales.append({
            'sale_id':len(self.sales) + 1,
            'sale_name':request.json['sale_name'],
            'price': request.json['price'],
            'quantity':request.json['quantity'],
            'category':request.json['category'],
            'total':request.json['total']
        })

    def get_all_orders(self):
        return self.sales

    def get_a_single_order_with_id(self,id):
         for sale in self.sales:
            if sale['sale_id'] == id:
                self.sales.append(sale)

    def delete_order_with_id(self,id):
        for sale in self.sales:
            if sale['sale_id'] == id:
                self.sales.remove(sale)

    def delete_all_orders(self):
        self.sales.remove(Sale)
        

class User():

    def __init__(self, user_id, username, password, gender):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.gender = gender

    def register(self):
        new_user = {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "gender": self.gender

        }

        users.append(new_user)
        return jsonify(users)




       
