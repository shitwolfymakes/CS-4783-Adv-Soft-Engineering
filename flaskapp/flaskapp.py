from flask import Flask
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint
from routes import register_views


def main():
    app = Flask(__name__)

    ### start swagger boilerplate ###
    swagger_url = '/swagger'
    api_url = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "flaskapp"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

    register_views(app)     # registration needs to happen before running the app
    CORS(app)   # enabling CORS requests
    app.run()
#end main


if __name__ == "__main__":
    main()
