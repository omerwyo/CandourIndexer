from ast import Str
from project.routes.database import db
import datetime

'''
    Deserialize datetime object into string form for JSON processing.
'''
def dump_datetime(value):
    if value is None:
        return None
    return value.strftime("%d %b %Y, %H:%M")

class TextPickleType(db.PickleType):
    impl = db.Text

# ------------------------------------------------------------------- #
# This product object is each of the products that we can see in our product discovery page
class Product(db.Model):
    __tablename__='product'

    batchNo = db.Column(db.String, primary_key=True, nullable=False)
    stage_one = db.Column(db.PickleType(TextPickleType))
    stage_two = db.Column(db.PickleType(TextPickleType))
    productName = db.Column(db.String, nullable=True)
    imageUrl = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    is_completed = db.Column(db.Boolean, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, batchNo, fertiliser_type, fertiliser_used, water_consumption, biowaste, location) -> None:
        self.batchNo = batchNo

        # Stage 1 Attributes; we pass in the details for the very first stage with the creation of the product object
        self.stage_one = {"fertiliser_type": fertiliser_type,
                          "fertiliser_used": fertiliser_used,
                          "water_consumption": water_consumption,
                          "biowaste": biowaste,
                          "location": location}
        # Stage 2 Attributes; default, to be updated incrementally
        self.stage_two = {"water_consumption": "",
                          "electricity_used": "",
                          "effluent_released": ""}
        self.productName = ""
        self.imageUrl = ""
        self.description = ""
        self.is_completed = False
        self.last_updated = datetime.datetime.now()

    def __repr__(self) -> str:
        return f'Product #{self.batchNo}, Last Updated: {self.last_updated}'

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'batchNo': self.batchHash,
            'stage_one': self.stage_one,
            'stage_two': self.stage_two,
            'last_updated': dump_datetime(self.last_updated),
            'is_completed': self.is_completed,
            'productName': self.productName,
            'imageUrl': self.imageUrl,
            'description': self.description
        }
# ------------------------------------------------------------------- #