"""Provides database access functionality"""

import json
import pyodbc
import pymysql
import pymysql.cursors


class DBGateway:
    def __init__(self):
        self.db_creds = {}

        with open('dbcreds.json') as infile:
            self.db_creds = json.load(infile)

        self._conn = pymysql.connect(host=self.db_creds['url'],
                                     user=self.db_creds['user'],
                                     password=self.db_creds['pass'],
                                     port=self.db_creds['port'],
                                     db=self.db_creds['db'])
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                   "Server=localhost,12138;" +
                                   "Database=assignment4;" +
                                   "Trusted_Connection=yes;")
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
