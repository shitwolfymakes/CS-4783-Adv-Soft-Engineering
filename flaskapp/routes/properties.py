import flask
#import flask_api
import flask_restful
from flask import request, jsonify #,Response
from flask_api import status
#from flask_mysqldb import MySQL    #ToDO SQL integration
from flask_restful import reqparse
currentDir = ""

app = flask.current_app
bp = flask.Blueprint("properties", __name__)

def prepareResponse(tag, msg):
    response = [{
            tag: msg
    }]
    return jsonify(response)

@bp.route('/properties', methods=['GET', 'POST'])
def addProperty():
    if request.method == 'GET':
        #TODO Get from SQL DB
        return prepareResponse("message", "id SOMETHING"), status.HTTP_200_OK

    elif request.method == 'POST':
        req_data = request.get_json(force=True)
        address = req_data['address']
        city = req_data['city']
        state = req_data['state']
        zip = req_data['zip']
        #TODO auto assign ID
        if(len(address) >= 1 and len(address) <= 200 and len(state) == 2 and len(city) >= 1 and len(city) <= 50 and len(zip) >= 5 and len(zip) <= 10):
                return prepareResponse("message", "added"), status.HTTP_200_OK
        elif(len(address) < 1 or len(address) > 200):
            return prepareResponse("message", "address is not between 1 and 200 characters"), status.HTTP_400_BAD_REQUEST
        elif(len(city) < 1 or len(city) > 50):
            return prepareResponse("message", "city is not between 1 and 50 characters"), status.HTTP_400_BAD_REQUEST
        elif (len(state) != 2):
            return prepareResponse("message", "state is not 2 characters"), status.HTTP_400_BAD_REQUEST
        elif (len(zip) < 5 or len(zip) > 10):
            return prepareResponse("message", "zip is not between 5 and 10 characters"), status.HTTP_400_BAD_REQUEST

#end properties


