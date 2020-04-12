"""
This file contains the code for www.flaskappurl.com/hello
"""
import flask
from flask import jsonify
from flask_api import status

app = flask.current_app
bp = flask.Blueprint("hello", __name__)


def prepare_response(tag, msg):
    response = [{
            tag: msg
    }]
    return jsonify(response)
#end prepare_response


@bp.route("/hello")
def hello():
    return prepare_response("message", "hello yourself"), status.HTTP_200_OK
#end hello
