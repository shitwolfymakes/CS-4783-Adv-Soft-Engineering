#!/bin/bash

#start the daemon
mysqld_safe &

#get PID to kill later
/usr/share/mysql/mysql.server start