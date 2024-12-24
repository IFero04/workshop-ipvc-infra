-- Switch the database
\c airport;

-- Air Routes table
CREATE TABLE air_routes (
    id              serial PRIMARY KEY,
	xml             XML NOT NULL,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);