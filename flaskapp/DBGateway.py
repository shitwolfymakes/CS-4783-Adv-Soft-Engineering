"""Provides database access functionality"""

import pymysql
import pymysql.cursors
import mysql.connector


class DBGateway:
    def __init__(self):
        config = {
            "user": "root",
            "password": "@ss1gnmentFour",
            "host": "localhost",
            "port": '12138',
            "database": "assignment4"
        }

        self._conn = mysql.connector.connect(**config)
    #end init


    def get_connection(self):
        return self._conn
    #end get_connection
#end class DBGateway


# Testing Harness Below Here #
def main():
    gateway = DBGateway()
    #print(gateway.db_creds)
    conn = gateway.get_connection()
    with conn.cursor() as cursor:
        sql = "SELECT * FROM tbl_props"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
#end main


if __name__ == '__main__':
    main()
