FROM postgres:13

ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=habr
ENV POSTGRES_DB=my_db


ADD ./docker-entrypoint-initdb.d/couriers_db_dump.sql /docker-entrypoint-initdb.d/