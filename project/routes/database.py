import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from project.routes.models import Product

# ------------------------------------------------------------------- #
'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + os.environ.get('DATABASE_URL')[len('postgresql/'):]
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
# ------------------------------------------------------------------- #
'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
# ------------------------------------------------------------------- #