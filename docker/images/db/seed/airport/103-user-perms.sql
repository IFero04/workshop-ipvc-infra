-- Conceder privilégios no banco de dados
GRANT CONNECT ON DATABASE airport TO mule;
\c airport;

-- Conceder privilégios nas tabelas
GRANT USAGE ON SCHEMA public TO mule;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE air_routes TO mule;
