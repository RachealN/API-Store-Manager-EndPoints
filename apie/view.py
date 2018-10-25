from flask import Flask, request, jsonify, abort, make_response
from apie.models.model import Product, Sale, Admin, StoreAttendant
# from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config["DEBUG"] = True
# auth = HTTPBasicAuth()



products = []
sales = []


# @auth.get_password
# def get_password(username):
#     if username == 'Racheal':
#         return 'rac'
#     return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error':'unauthorized access'}),400)


@app.route('/', methods=['GET'])
def home():
    return ('Welcome to Store Manager'),200


@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message': 'Requested method not allowed'}), 405


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'page not found, check the url'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'internal server error'}), 500


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'product not found'}), 404)


@app.route('/api/v1/product/', methods=['POST'])
# @auth.login_required
def create_product():
    product = {
        'id': request.json['id'] + 1,
        'product_name': request.json['product_name'],
        'price': request.json['price'],
        'quantity': request.json['quantity'],
        'category': request.json['category'],
    }

    if not product['product_name']:
        return jsonify({'message': "Name can not be empty"}), 400


    data = products.append(product)
    return jsonify({'data': product, 'message': "succesfully added"}), 201


@app.route('/api/v1/products/all', methods=['GET'])
# @auth.login_required
def products_all():
    return jsonify(products)


@app.route('/api/v1/products/<pk>/', methods=['GET'])
# @auth.login_required
def products_id(pk):
    try:
        int(pk)
    except:
        return jsonify({"error": "id input should be an integer"})

    for dict in products:
        if dict['id'] == int(pk):
            return jsonify(dict)

    else:
        return jsonify({"message": "The product with that id was not found"})


@app.route('/api/v1/product/<int:product_id>', methods=['PUT'])
# @auth.login_required
def update_product(product_id):
    product = [product for product in products if int(
        product['id']) == int(product_id)]
    product[0]['name'] = request.json.get('name')
    product[0]['category'] = request.json.get('category')
    if len(product) == 0:
        abort(404)
    if not product[0]['name']:
        abort(400)

    return jsonify({'data': product, 'message': "succesfully updated"}), 200


@app.route('/api/v1/product/<int:product_id>', methods=['DELETE'])
# @auth.login_required
def delete_product(product_id):
    product = [product for product in products if int(
        product['id']) == int(product_id)]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'message': "succesfully deleted"})


@app.route('/api/v1/sale/', methods=['POST'])
# @auth.login_required
def create_sales():
    sale = {
        'id': request.json['id'] + 1,
        'sale_name': request.json['sale_name'],
        'price': request.json['price'],
        'quantity': request.json['quantity'],
        'category': request.json['category'],
        'total':request.json['total']
    }
    if not sale['sale_name']:
        return jsonify({'message': "Name can not be empty"}), 400

    data = sales.append(sale)
    return jsonify({'data': sales, 'message': "succesfully added"}), 201


@app.route('/api/v1/sales/all', methods=['GET'])
# @auth.login_required
def sales_all():
    return jsonify(sales)


@app.route('/api/v1/sales/<pk>/', methods=['GET'])
# @auth.login_required
def sales_id(pk):
    try:
        int(pk)
    except:
        return jsonify({"error": "id input should be an integer"})

    for dict in sales:
        if dict['id'] == int(pk):
            return jsonify(dict)

    else:
        return jsonify({"message": "The sales with that id was not found"})

                                                                                                                                                                                                                                                                                                                                    



