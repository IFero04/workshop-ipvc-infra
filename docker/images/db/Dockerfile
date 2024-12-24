FROM postgres:15.5-alpine3.18

COPY seed/global/* /docker-entrypoint-initdb.d/
COPY seed/airport/* /docker-entrypoint-initdb.d/
