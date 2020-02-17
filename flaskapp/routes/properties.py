import flask
from flask import request, jsonify
from flask_api import status
import pymysql

from DBGateway import DBGateway

currentDir = ""

app = flask.current_app
bp = flask.Blueprint("properties", __name__)


def prepare_response(tag, msg):
    response = [{
            tag: msg
    }]
    return jsonify(response)


@bp.route('/properties', methods=['GET', 'POST'])
def add_property():
    if request.method == 'GET':
        cur = None
        conn = None
        try:
            gateway = DBGateway()
            conn = gateway.get_connection()
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
        #end try/except/finally
    elif request.method == 'POST':
        req_data = request.get_json(force=True)
        address = req_data['address']
        city = req_data['city']
        state = req_data['state']
        zip_code = req_data['zip']

        if 1 <= len(address) <= 200 and len(state) == 2 and 1 <= len(city) <= 50 and 5 <= len(zip_code) <= 10:
            cur = None
            conn = None
            try:
                sql = "INSERT INTO tbl_property(ID, address, city, state, zip) VALUES(NULL, %s, %s, %s, %s)"
                data = (address, city, state, zip_code)
                gateway = DBGateway()
                conn = gateway.get_connection()
                cur = conn.cursor()
                cur.execute(sql, data)
                conn.commit()
                return prepare_response("message", "added"), status.HTTP_200_OK
            except Exception as e:
                print(e)
            finally:
                cur.close()
                conn.close()
            #end try/except/finally
        #end if

        if len(address) < 1 or len(address) > 200:
            return prepare_response("message", "address is not between 1 and 200 characters"), status.HTTP_400_BAD_REQUEST
        if len(city) < 1 or len(city) > 50:
            return prepare_response("message", "city is not between 1 and 50 characters"), status.HTTP_400_BAD_REQUEST
        if len(state) != 2:
            return prepare_response("message", "state is not 2 characters"), status.HTTP_400_BAD_REQUEST
        if len(zip_code) < 5 or len(zip_code) > 10:
            return prepare_response("message", "zip is not between 5 and 10 characters"), status.HTTP_400_BAD_REQUEST
    #end if/elif
#end properties


@bp.route('/properties/<int:property_id>', methods=['GET', 'DELETE'])
def id_property(property_id):
    if request.method == 'GET':
        cur = None
        conn = None
        try:
            gateway = DBGateway()
            conn = gateway.get_connection()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM tbl_property WHERE ID=%s", property_id)
            rows = cur.fetchall()
            if not rows:
                return prepare_response("ID does not exist in database.", status.HTTP_404_NOT_FOUND)
            response = jsonify(rows)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
        # end try/except/finally
    elif request.method == 'DELETE':
        cur = None
        conn = None
        try:
            gateway = DBGateway()
            conn = gateway.get_connection()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("DELETE FROM tbl_property WHERE ID=%s", property_id)
            conn.commit()
            return prepare_response("message", "deleted"), status.HTTP_200_OK
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
        # end try/except/finally
    # end if/elif
#end properties property_id


@bp.errorhandler(404)
def not_found(error=None):
    return prepare_response("message", "not found"), status.HTTP_404_NOT_FOUND
# end not_found
