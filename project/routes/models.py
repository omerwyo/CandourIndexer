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
        
    # def encode_auth_token(self, user_id):
    #     '''
    #     Generates the Auth Token
    #     :return: string
    #     '''
    #     try:
    #         payload = {
    #             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
    #             'iat': datetime.datetime.utcnow(),
    #             'sub': user_id
    #         }
    #         return jwt.encode(
    #             payload,
    #             app.config['SECRET_KEY'],
    #             algorithm='HS256'
    #         )
    #     except Exception as e:
    #         return e

    # @staticmethod
    # def decode_auth_token(auth_token):
    #     """
    #     Decodes the auth token
    #     :param auth_token:
    #     :return: integer|string
    #     """
    #     try:
    #         payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
    #         return payload['sub']
    #     except jwt.ExpiredSignatureError:
    #         return 'Signature expired. Please log in again.'
    #     except jwt.InvalidTokenError:
    #         return 'Invalid token. Please log in again.'
# ------------------------------------------------------------------- #