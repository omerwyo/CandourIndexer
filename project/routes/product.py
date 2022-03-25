from datetime import timedelta
from itertools import product
from flask import request, jsonify, make_response
from project import app
from project.routes.models import Product
from project.routes.database import db

# ------------------------------------------------------------------- #
# bookkeep a product with the specified hash
@app.route('/product', methods=['POST'])
def register():
    post_data = request.get_json()

    # check if user already exists
    product = Product.query.filter_by(batchHash=post_data.get('hash')).first()
    if product: 
        responseObject = {
            'status': 'fail',
            'message': 'Product with Hash '+ post_data.get('hash') + ' already exists',
        }
        return make_response(jsonify(responseObject)), 202
    else:
        try:
            # Commit the product to our DB
            product = Product(
                batchHash=post_data.get('hash'),
                productName=post_data.get('name'),
                password=post_data.get('password'),
                imageUrl=post_data.get('imageUrl'),
                description=post_data.get('description')
            )
            # insert the user
            db.session.add(product)
            db.session.commit()
            responseObject = {
                'status': 'Success',
                'message': 'Product was successfully added'
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'Failed',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 400
# ------------------------------------------------------------------- #