from flask import Flask

from routes import register_views


def main():
    app = Flask(__name__)
    register_views(app)     # registration needs to happen before running the app
    app.run()
#end main


if __name__ == "__main__":
    main()
