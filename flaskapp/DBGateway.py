"""Provides database access functionality"""

import json
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
                                     db=self.db_creds['user'])
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
        sql = "SELECT * FROM `tbl_property`"
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)

#end main


if __name__ == '__main__':
    main()
