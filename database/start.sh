#!/bin/bash

#start the db server in BG
/opt/mssql/bin/sqlservr &

#get the process id for sql server in BG (to kill it later)
last_pid=$!

#wait for db startup
sleep 15

#import db schems and data
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Ass!gnment4 -i /mydb/mydb.sql

#stop db server BG
kill -KILL $last_pid

#start db server FG
/opt/mssql/bin/sqlservr