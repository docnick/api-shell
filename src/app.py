import logging
from flask import Flask
from flask.ext import restful
from werkzeug.contrib.fixers import ProxyFix
import resources.sample_endpoints as endpoints


APP = Flask(__name__)
API = restful.Api(APP)


# GET
API.add_resource(endpoints.Test, '/test')


def init_logging():
    logger = logging.getLogger()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # handler = logging.FileHandler("/var/log/test-api.log")
    # handler.setFormatter(formatter)
    # handler.setLevel(logging.DEBUG)
    # logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    init_logging()
    logging.debug("In __main__, running host...")
    APP.run(host='0.0.0.0', debug=True)

elif __name__ == 'app':
    # when we run using gunicorn
    init_logging()
    logging.debug("WSGI setup...")
    APP.wsgi_app = ProxyFix(APP.wsgi_app)
    logging.debug("Running host")
