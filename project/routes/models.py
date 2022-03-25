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

    batchHash = db.Column(db.String, primary_key=True, nullable=False)
    productName = db.Column(db.String, nullable=False)
    completed_on = db.Column(db.DateTime, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, batchHash, productName, imageUrl, description) -> None:
        self.batchHash = batchHash
        self.productName = productName
        self.imageUrl = imageUrl
        self.description = description
        self.completed_on = datetime.datetime.now()

    def __repr__(self) -> str:
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