

class Product:
    def __init__(self):
          self.products = []
    

    def get_product(self):
        return self.products

    def get_one_product(self, id):
        for item in self.products:
            if item['id'] == id:
                return item

    def get_product_name(self,product_name):
        for item in self.products:
            if item['product_name'] == product_name:
                return item
       
        
class Sale:
    def __init__(self):
        self.sales = []

    def get_sale(self):
        return self.sales

    def get_single_sale(self,sale_name):
        for item in self.sales:
            if item['sale_name'] == sale_name:
                return item


class StoreUsers():
    def __init__(self):
        self.users = []
        

class Admin(StoreUsers):
    def __init__(self):
        self.users = []

    def get_admin_user_id(self,user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return user

    def get_admin_username(self,username):
        for user in self.users:
            if user['username'] == username:
                return user

    def get_admin_pasword(self,password):
        for user in self.users:
            if user['password'] == password:
                return user

class StoreAttendant(StoreUsers):
    def __init__(self, username):
        self.users = []

    def get_attendant_username(self,username):
        for user in self.users:
            if user['username'] == username:
                return user

    def get_attendant_password(self,password):
        for user in self.users:
            if user['password'] == password:
                return user
       

        
