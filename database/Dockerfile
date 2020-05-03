FROM microsoft/mssql-server-linux:2017-latest

ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=assignmentFour
ENV MSSQL_PID=Developer
ENV MSSQL_TCP_PORT=1433

WORKDIR /src

COPY mydb.sql /mydb/
COPY start.sh /mydb/

EXPOSE 1433

CMD /bin/bash /mydb/start.sh