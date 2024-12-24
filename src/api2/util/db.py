import json
from datetime import date
from db.database import SQLite
from db.operations import get_all_air_routes, create_air_route
from db.models import AirRoute
from util.config import settings


def start_db_data():
    with SQLite(settings.API2_DATABASE_URL) as session:
        routes = get_all_air_routes(session)
        if routes:
            session.query(AirRoute).delete()
            session.commit()

        try:
            with open("/data/api2.json", "r") as file:
                data = json.load(file)

            for route in data:
                create_air_route(
                    from_location=route["from"],
                    to_location=route["to"],
                    airport=route["airport"],
                    seats_available=route["seats_available"],
                    plane_number=route["plane_number"],
                    port_number=route["port_number"],
                    fly_code=route["fly_code"],
                    route_date=date.fromisoformat(route["date"]),
                    session=session
                )

        except FileNotFoundError:
            print("Error: api2.json file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in api2.json.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
