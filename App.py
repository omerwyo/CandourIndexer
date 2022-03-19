import logging
from project import app

logger = logging.getLogger(__name__)
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# ------------------------------------------------------------------- #
# homepage
@app.route('/', methods=['GET'])
def home():
    return '''<h1>hello!</h1>'''

# ------------------------------------------------------------------- #
if __name__ == "__main__":
    # logging.info("Starting application ...")
    app.run(debug=False, port=33507)