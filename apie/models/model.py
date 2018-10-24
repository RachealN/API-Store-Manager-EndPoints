

class Product:
    def __init__(self, id, product_name, price=int, quantity=int):
        self.id = id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def get_product(self):
        return{
            "id": self.id,
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity
        }


class Sale:
    def __init__(self, id, sale_name, price, quantity, total):
        self.id = id
        self.sale_name = sale_name
        self.price = price
        self.quantity = quantity
        self.total = total

    def get_sale(self):
        return{
            "id": self.id,
            "sale_name": self.sale_name,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total
        }


class StoreUsers():
    def __init__(self, users_id, username, password, store_name):
        self.users_id = users_id,
        self.username = username,
        self.password = password,
        self.store_name = store_name
        

class Admin(StoreUsers):
    def __init__(self, store_name, username, password):
        super().__init__(store_name, username,password)
        self.store_name = store_name
        self.username = username
        self.password = password

class StoreAttendant(StoreUsers):
    def __init__(self,users_id, username, password):
        super().__init__(users_id, username, password)
        self.users_id = users_id
        self.username = username
        self.password = password

        
