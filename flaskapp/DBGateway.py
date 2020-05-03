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

        #self._conn = mysql.connector.connect(**config)
        self._conn = pymysql.connect(host="mysqldb",
                                     user="root",
                                     password="@ss1gnmentFour",
                                     port=3306,
                                     db="assignment4")
    #end init


    def get_connection(self):
        return self._conn
    #end get_connection
#end class DBGateway


# Testing Harness Below Here #
def main():
    #gateway = DBGateway()
    #print(gateway.db_creds)
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="@ss1gnmentFour",
                           port=12138,
                           db="assignment4")
    with conn.cursor() as cursor:
        sql = "SELECT * FROM tbl_props"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
#end main


if __name__ == '__main__':
    main()
