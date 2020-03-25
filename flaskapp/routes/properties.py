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
        _handle_add_property_get()
    elif request.method == 'POST':
        _handle_add_property_post()
#end add_property


def _handle_add_property_get():
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
    # end try/except/finally
#end _handle_add_property_get


def _handle_add_property_post():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'cs4783FTW':
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
            # end try/except/finally
        if len(address) < 1 or len(address) > 200:
            return prepare_response("message", "address is not between 1 and 200 characters"), status.HTTP_400_BAD_REQUEST
        if len(city) < 1 or len(city) > 50:
            return prepare_response("message", "city is not between 1 and 50 characters"), status.HTTP_400_BAD_REQUEST
        if len(state) != 2:
            return prepare_response("message", "state is not 2 characters"), status.HTTP_400_BAD_REQUEST
        if len(zip_code) < 5 or len(zip_code) > 10:
            return prepare_response("message", "zip is not between 5 and 10 characters"), status.HTTP_400_BAD_REQUEST
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    # end if/else
#end _handle_add_property_post


@bp.route('/properties/<property_id>', methods=['GET', 'DELETE', 'PUT'])
def id_property(property_id):
    try:
        property_id = int(property_id)
        if not isinstance(property_id, int):
            return prepare_response("message", "ID is not an integer"), status.HTTP_400_BAD_REQUEST
    except ValueError:
        return prepare_response("message", "ID is not an integer"), status.HTTP_400_BAD_REQUEST
    #end try/catch
    
    if request.method == 'GET':
        _handle_id_property_get(property_id)
    elif request.method == 'DELETE':
        _handle_id_property_delete(property_id)
    elif request.method == 'PUT':
        _handle_id_property_put(property_id)
    #end if/elif
#end properties property_id


def _handle_id_property_get(property_id):
    cur = None
    conn = None
    try:
        gateway = DBGateway()
        conn = gateway.get_connection()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        # check to see if the property exists
        cur.execute("SELECT * FROM tbl_property WHERE ID=%s", property_id)
        rows = cur.fetchall()
        if not rows:
            return prepare_response("message", "ID does not exist in database."), status.HTTP_404_NOT_FOUND

        response = jsonify(rows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    # end try/except/finally
#end _handle_id_property_get


def _handle_id_property_delete(property_id):
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'cs4783FTW':
        cur = None
        conn = None
        try:
            gateway = DBGateway()
            conn = gateway.get_connection()
            cur = conn.cursor(pymysql.cursors.DictCursor)

            # check to see if the property exists
            cur.execute("SELECT * FROM tbl_property WHERE ID=%s", property_id)
            rows = cur.fetchall()
            if not rows:
                return prepare_response("message", "ID does not exist in database."), status.HTTP_404_NOT_FOUND

            # delete the property if it does
            cur.execute("DELETE FROM tbl_property WHERE ID=%s", property_id)
            conn.commit()
            return prepare_response("message", "deleted"), status.HTTP_200_OK
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
        # end try/except/finally
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    # end if/else
#end _handle_id_property_delete


def _handle_id_property_put(property_id):
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'cs4783FTW':
        # req_data = request.get_json(force=True)
        cur = None
        conn = None
        try:
            gateway = DBGateway()
            conn = gateway.get_connection()
            cur = conn.cursor(pymysql.cursors.DictCursor)

            # check to see if the property exists
            cur.execute("SELECT * FROM tbl_property WHERE ID=%s", property_id)
            rows = cur.fetchall()
            if not rows:
                return prepare_response("message", "ID does not exist in database."), status.HTTP_404_NOT_FOUND

            # update the property if it does
            req_data = request.get_json(force=True)
            for ans in req_data:
                # print (ans) to test, allows optional arguments
                if ans == 'address':
                    address = req_data['address']
                    if 1 <= len(address) <= 200:
                        cur.execute("UPDATE tbl_property SET address = %s WHERE ID = %s", (address, property_id))
                        conn.commit()
                if ans == 'state':
                    state = req_data['state']
                    if len(state) == 2:
                        cur.execute("UPDATE tbl_property SET state = %s WHERE ID = %s", (state, property_id))
                        conn.commit()
                if ans == 'city':
                    city = req_data['city']
                    if 1 <= len(city) <= 50:
                        cur.execute("UPDATE tbl_property SET city = %s WHERE ID = %s", (city, property_id))
                        conn.commit()
                if ans == 'zip':
                    zip_code = req_data['zip']
                    if 5 <= len(zip_code) <= 10:
                        cur.execute("UPDATE tbl_property SET zip = %s WHERE ID = %s", (zip_code, property_id))
                        conn.commit()
            #end for
            return prepare_response("message", "updated"), status.HTTP_200_OK
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
        # end try/except/finally
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    # end if/else
#end _handle_id_property_delete


@bp.errorhandler(404)
def not_found(error=None):
    return prepare_response("message", "not found"), status.HTTP_404_NOT_FOUND
# end not_found
