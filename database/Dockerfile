FROM mysql:8.0.19

ENV MYSQL_DATABASE=assignment4
ENV MYSQL_ROOT_PASSWORD=@ss1gnmentFour

COPY mysqldb.sql /docker-entrypoint-initdb.d

WORKDIR /db

COPY . /db
CMD ["/bin/bash", "start.sh"]

EXPOSE 3306
