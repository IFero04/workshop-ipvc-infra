from fastapi import APIRouter, status, HTTPException
from db.database import SQLite
from db.operations import get_all_air_routes, reserve_flight_route, cancel_flight_route
from util.config import settings


router = APIRouter()

def map_route_data(route):
    return {
        "id": route.id,
        "airport": route.airport,
        "from": route.from_location,
        "to": route.to_location,
        "plane_number": route.plane_number,
        "fly_code": route.fly_code,
        "seats_available": route.seats_available,
        "port_number": route.port_number,
        "date": route.date
    }

@router.get('/available', status_code=status.HTTP_200_OK)
def get_available_routes():
    try:
        with SQLite(settings.API1_DATABASE_URL) as session: 
            routes = get_all_air_routes(session)
            transformed_routes = [map_route_data(route) for route in routes]
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
    
    return {"message": "Air Routes available retrieved", "data": transformed_routes }

@router.patch('/reserve', status_code=status.HTTP_200_OK)
def reserve_flight(fly_code: str):
    try:
        with SQLite(settings.API1_DATABASE_URL) as session:
            reserve_flight_route(fly_code, session)
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
    
    return {"message": "Flight reserved successfully"}

@router.delete('/cancel', status_code=status.HTTP_200_OK)
def cancel_flight(fly_code: str):
    try:
        with SQLite(settings.API1_DATABASE_URL) as session:
            cancel_flight_route(fly_code, session)
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
    
    return {"message": "Flight canceled successfully"}