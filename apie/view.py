from flask import Flask, request, jsonify, abort, make_response
from apie.models.model import Product, Sale, User


app = Flask(__name__)
app.config["DEBUG"] = True



products = []
sales = []


@app.route('/', methods=['GET'])
def home():
    return ('Welcome to Store Manager'),200


@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message': 'Requested method not allowed'}), 405



@app.route('/api/v1/product/', methods=['POST'])
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


    products.append(product)
    return jsonify({'data': product, 'message': "succesfully added"}), 201


@app.route('/api/v1/products/all', methods=['GET'])
def products_all():
    return jsonify(products)


@app.route('/api/v1/products/<pk>/', methods=['GET'])
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
def delete_product(product_id):
    product = [product for product in products if int(
        product['id']) == int(product_id)]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'message': "succesfully deleted"})


@app.route('/api/v1/sale/', methods=['POST'])
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

    sales.append(sale)
    return jsonify({'data': sales, 'message': "succesfully added"}), 201


@app.route('/api/v1/sales/all', methods=['GET'])
def sales_all():
    return jsonify(sales)


@app.route('/api/v1/sales/<int:pk>/', methods=['GET'])
def sales_id(pk):
    try:
        int(pk)
    except:
        return jsonify({"error": "id input should be an integer"})

    for dict in sales:
        if dict['id'] == int(pk):
            return jsonify(dict)

    else:
        return jsonify({"message": "The sale with that id was not found"})

                                                                                                                                                                                                                                                                                                                                    



