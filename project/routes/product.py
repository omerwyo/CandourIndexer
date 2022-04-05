import datetime
import json
from flask import request, jsonify, make_response
from project import app
from project.routes.models import Product
from project.routes.database import db

# ------------------------------------------------------------------- #
# bookkeep a product with the specified hash
@app.route('/product', methods=['POST'])
def addProduct():
    post_data = request.get_json()

    # check if Product already exists
    product = Product.query.filter_by(batchNo=post_data.get('batchNo')).first()
    if product:
        try:
            # Initiate the update of a stage of this product (Entering in stage 2 + Product Discovery end's details)
            product.water_consumption_2 = post_data.get("water_consumption")
            product.electricity_used = post_data.get("electricity_used")
            product.effluent_released = post_data.get("effluent_released")
            product.productName = post_data.get("productName")
            product.imageUrl = post_data.get("imageUrl")
            product.description = post_data.get("description")
            product.last_updated = datetime.datetime.now()
            product.is_completed = True
            product.location_two = post_data.get("location_two")
            db.session.commit()
            responseObject = {
                'status': 'Success',
                'message': 'Product with batchNo '+ post_data.get('batchNo') + "'s stage 2 has been updated!",
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'Failed',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 400
    else:
        try:
            # Commit the product to our DB
            # We will be inputting stage 1 details at this point
            product = Product(
                batchNo=post_data.get('batchNo'),
                fertiliser_type=post_data.get('fertiliser_type'),
                fertiliser_used=post_data.get('fertiliser_used'),
                water_consumption=post_data.get('water_consumption'),
                biowaste=post_data.get('biowaste'),
                location=post_data.get('location')
            )
            # print(f'Product is: {product.serialize()}')
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

# ------------------------------------------------------------------- #
# get all products
@app.route('/getAll', methods=['GET'])
def getProducts():
    products = Product.query.all()
    return jsonify(products=[p.serialize() for p in products]), 200
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
# get product by batchno
@app.route('/product', methods=['GET'])
def getProductById():
    queryBatchNo = request.args.get('id')
    product = Product.query.get(queryBatchNo)
    if not product:
        responseObject = {
                'status': 'Failed',
                'message': f'Product with batchNo {queryBatchNo} doesn\'t exist'
            }
        return make_response(jsonify(responseObject)), 404
    else:
        responseObject = product
        return make_response(jsonify(product.serialize())), 200
# ------------------------------------------------------------------- #