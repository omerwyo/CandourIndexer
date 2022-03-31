from datetime import datetime
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
            product.stage_two["water_consumption"] = post_data.get("water_consumption")
            product.stage_two["electricity_used"] = post_data.get("electricity_used")
            product.stage_two["effluent_released"] = post_data.get("effluent_released")
            product.productName = post_data.get("productName")
            product.imageUrl = post_data.get("imageUrl")
            product.description = post_data.get("description")
            product.last_updated = datetime.datetime.now()
            product.is_completed = False
            db.session.commit()
            responseObject = {
                'status': 'Success',
                'message': 'Product with batchNo '+ post_data.get('batchNo') + "'s stage 2 has been updated!",
            }
            return make_response(jsonify(responseObject)), 200
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
@app.route('/product', methods=['GET'])
def getProducts():
    products = Product.query.all()
    return jsonify(products=[p.serialize() for p in products]), 200
# ------------------------------------------------------------------- #