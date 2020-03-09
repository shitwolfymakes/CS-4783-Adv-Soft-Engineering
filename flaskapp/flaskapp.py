import sys

from flask import Flask
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint
from routes import register_views


def main():
    using_https = False
    if "--cert=adhoc" in sys.argv:
        using_https = True
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
    if using_https:
        app.run(host="0.0.0.0", port=12137, ssl_context='adhoc')
    else:
        app.run(host="0.0.0.0", port=12137)
#end main


if __name__ == "__main__":
    main()
