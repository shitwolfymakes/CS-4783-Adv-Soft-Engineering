import flask
from flask import request, jsonify
from flask_api import status
import pymysql

#conn uses the login info also located in DBGateway.py
#example of post body for properties to use with Postman:
#{"address": "12367 Road Rd.", "city": "San AN", "state": "TX", "zip": "79992"}
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
        try:
            conn = pymysql.connect(host='easel2.fulgentcorp.com', port=3306, user='xne693', passwd='v3FPwOMciKr1dIoHvKUJ', db='xne693')
            cur = conn.cursor(pymysql.cursors.DictCursor)
            sql = "SELECT * FROM tbl_property"
            cur.execute(sql)
            rows = cur.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    elif request.method == 'POST':
        req_data = request.get_json(force=True)
        address = req_data['address']
        city = req_data['city']
        state = req_data['state']
        zip = req_data['zip']

        if(len(address) >= 1 and len(address) <= 200 and len(state) == 2 and len(city) >= 1 and len(city) <= 50 and len(zip) >= 5 and len(zip) <= 10):
            try:
                sql = "INSERT INTO tbl_property(ID, address, city, state, zip) VALUES(NULL, %s, %s, %s, %s)"
                data = (address, city, state, zip)
                conn = pymysql.connect(host='easel2.fulgentcorp.com', port=3306, user='xne693', passwd='v3FPwOMciKr1dIoHvKUJ', db='xne693')
                cur = conn.cursor()
                cur.execute(sql, data)
                conn.commit()
                return prepareResponse("message", "added"), status.HTTP_200_OK
            except Exception as e:
                print (e)
            finally:
                cur.close()
                conn.close()

        if(len(address) < 1 or len(address) > 200):
            return prepareResponse("message", "address is not between 1 and 200 characters"), status.HTTP_400_BAD_REQUEST
        if(len(city) < 1 or len(city) > 50):
            return prepareResponse("message", "city is not between 1 and 50 characters"), status.HTTP_400_BAD_REQUEST
        if (len(state) != 2):
            return prepareResponse("message", "state is not 2 characters"), status.HTTP_400_BAD_REQUEST
        if (len(zip) < 5 or len(zip) > 10):
            return prepareResponse("message", "zip is not between 5 and 10 characters"), status.HTTP_400_BAD_REQUEST

#end properties


