FROM mysql/mysql-server:latest
ENV MYSQL_ROOT_PASSWORD=1234 \
	MYSQL_DATABASE=microservice \
	MYSQL_USER=mysql \
	MYSQL_PASSWORD=mysql
COPY init.sql /docker-entrypoint-initdb.d