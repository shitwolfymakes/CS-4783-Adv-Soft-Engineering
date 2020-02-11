"""
This file contains the code for www.flaskappurl.com/
"""
import flask

app = flask.current_app
bp = flask.Blueprint("hello", __name__)


@bp.route("/")
def hello():
    return "Hello World!"
#end hello
