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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    isVerified = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, name, password, isVerified=False):
        self.email = email
        self.name = name
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.datetime.now()

    def __repr__(self):
        return f'User #{self.id}({self.email}, {self.name}'

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
    
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'email': self.email,
            'name': self.name,
            'dateCreated': dump_datetime(self.registered_on),
        }
# ------------------------------------------------------------------- #