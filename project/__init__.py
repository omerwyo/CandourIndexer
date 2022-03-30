from flask import Flask, jsonify, redirect, abort, request, make_response, session
from project.routes.database import setup_db, db_drop_and_create_all
from flask_cors import CORS
import os

# ------------------------------------------------------------------- #
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # Allow CORS
    CORS(app)

    setup_db(app)
    """ uncomment at the first time running the app """
    db_drop_and_create_all()

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500

    return app
# ------------------------------------------------------------------- #

app = create_app()

import project.routes.product