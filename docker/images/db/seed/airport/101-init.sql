-- Create the database and switch to it
CREATE DATABASE airport;

\c airport;
-- Create necessary extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
