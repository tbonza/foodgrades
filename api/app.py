import os
from flask import Flask

def create_app(config_module=None):
    app = Flask(__name__)
    app.config.from_object(config_module or
                           os.environ.get('FLASK_CONFIG') or
                           'config')

    from api.v1_0 import api_1_0 as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

    from api.v1_1 import api_1_1 as api_blueprint2
    app.register_blueprint(api_blueprint2, url_prefix='/api/v1.1')

    return app
