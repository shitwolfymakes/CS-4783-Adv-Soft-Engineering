"""Provides database access functionality"""

import json
import pymysql


class DBGateway:
    def __init__(self):
        self.db_creds = {}

        with open('dbcreds.json') as infile:
            self.db_creds = json.load(infile)

        conn = pymysql.connect(host=self.db_creds['url'],
                               user=self.db_creds['user'],
                               password=self.db_creds['pass'],
                               db=self.db_creds['user'])
    #end init
#end class DBGateway


# Testing Harness Below Here #
def main():
    gateway = DBGateway()
    print(gateway.db_creds)

#end main


if __name__ == '__main__':
    main()
