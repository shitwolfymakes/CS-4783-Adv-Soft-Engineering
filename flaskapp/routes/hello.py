"""
This file contains the code for www.flaskappurl.com/
"""
import flask
from flask import request, jsonify
from flask_api import status

app = flask.current_app
bp = flask.Blueprint("hello", __name__)

def prepareResponse(tag, msg):
    response = [{
            tag: msg
    }]
    return jsonify(response)

@bp.route("/hello")
def hello():
    return prepareResponse("message", "hello yourself"), status.HTTP_200_OK
#end hello
