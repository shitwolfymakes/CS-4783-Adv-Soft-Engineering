#use mysql official image
FROM mysql

#add a database
ENV MYSQL_DATABASE assignment5

WORKDIR /flaskapp

COPY mysqldb.sql /mydb/
COPY start.sh /mydb/

CMD /bin/bash /mydb/start.sh
