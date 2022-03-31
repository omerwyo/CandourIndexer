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

# ------------------------------------------------------------------- #
# This product object is each of the products that we can see in our product discovery page
class Product(db.Model):
    __tablename__='product'

    batchNo = db.Column(db.String, primary_key=True, nullable=False)
    stage_one = db.Column(db.PickleType(mutable=True), nullable=False)
    stage_two = db.Column(db.PickleType(mutable=True), nullable=False)
    productName = db.Column(db.String, nullable=True)
    imageUrl = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, batchNo, fertiliser_type:str, fertiliser_used:int, water_consumption:int, biowaste:int) -> None:
        self.batchNo = batchNo

        # Stage 1 Attributes; we pass in the details for the very first stage with the creation of the product object
        self.stage_one = {"fertiliser_type": fertiliser_type,
                          "fertiliser_used": fertiliser_used,
                          "water_consumption": water_consumption,
                          "biowaste": biowaste}
        # Stage 2 Attributes; default, to be updated incrementally
        self.stage_two = {"water_consumption": None,
                          "electricity_used": None,
                          "effluent_released": None}
        self.productName = None
        self.imageUrl = None
        self.description = None
        self.is_completed = False
        self.last_updated = datetime.datetime.now()

    def __repr__(self) -> str:
        return f'Product #{self.batchHash}({self.productName}, {self.completed_on}'

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'batchHash': self.batchHash,
            'productName': self.productName,
            'dateCreated': dump_datetime(self.completed_on),
            'description': self.description,
            'imageUrl': self.imageUrl
        }
# ------------------------------------------------------------------- #