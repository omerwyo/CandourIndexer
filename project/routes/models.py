from project.__init__ import app
from project.routes.database import db
import datetime

'''
    Deserialize datetime object into string form for JSON processing.
'''
def dump_datetime(value):
    if value is None:
        return None
    return value.strftime("%d %b %Y, %H:%M")
# ------------------------------------------------------------------- #

# This product object is each of the products that we can see in our product discovery page
class Product(db.Model):
    __tablename__='products'

    batchHash = db.Column(db.String, primary_key=True)
    productName = db.Column(db.String, nullable=False)
    completed_on = db.Column(db.DateTime, nullable=False)
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # isVerified = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.completed_on = datetime.datetime.now()

    def __repr__(self):
        return f'Product #{self.batchHash}({self.productName}, {self.completed_on}'

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'batchHash': self.batchHash,
            'productName': self.productName,
            'dateCreated': dump_datetime(self.completed_on),
        }

# ------------------------------------------------------------------- #