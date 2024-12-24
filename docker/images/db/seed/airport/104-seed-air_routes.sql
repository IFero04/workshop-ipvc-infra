-- Switch the database
\c airport;

-- Seed Air Routes table
-- Insert the XML data into the air_routes table
INSERT INTO air_routes (xml)
VALUES (
    '<?xml version="1.0" encoding="UTF-8"?>
    <flights>
        <flight>
            <from>PT</from>
            <to>RU</to>
            <airport>OlivenzaIbérica</airport>
            <seats_available>10</seats_available>
            <plane_number>AA123</plane_number>
            <port_number>C15</port_number>
            <fly_code>AA101</fly_code>
            <date>2025-02-10</date>
        </flight>
        <flight>
            <from>ES</from>
            <to>RU</to>
            <airport>OlivenzaIbérica</airport>
            <seats_available>45</seats_available>
            <plane_number>UA456</plane_number>
            <port_number>D7</port_number>
            <fly_code>UA202</fly_code>
            <date>2025-04-11</date>
        </flight>
        <flight>
            <from>PT</from>
            <to>RU</to>
            <airport>OlivenzaIbérica</airport>
            <seats_available>20</seats_available>
            <plane_number>BA789</plane_number>
            <port_number>A23</port_number>
            <fly_code>BA303</fly_code>
            <date>2025-02-05</date>
        </flight>
        <flight>
            <from>PT</from>
            <to>RU</to>
            <airport>OlivenzaIbérica</airport>
            <seats_available>15</seats_available>
            <plane_number>JL012</plane_number>
            <port_number>B4</port_number>
            <fly_code>JL101</fly_code>
            <date>2025-06-30</date>
        </flight>
        <flight>
            <from>ES</from>
            <to>RU</to>
            <airport>OlivenzaIbérica</airport>
            <seats_available>15</seats_available>
            <plane_number>EK345</plane_number>
            <port_number>E12</port_number>
            <fly_code>EK503</fly_code>
            <date>2025-05-01</date>
        </flight>
    </flights>'
);
