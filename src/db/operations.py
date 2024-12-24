from datetime import date
from fastapi import HTTPException, status
from sqlalchemy.orm import Session 
from .models import AirRoute


def create_air_route(
    from_location: str,
    to_location: str,
    airport: str,
    seats_available: int,
    plane_number: str,
    port_number: str,
    fly_code: str,
    route_date: date,
    session: Session
) -> AirRoute:
    new_route = AirRoute(
        from_location=from_location,
        to_location=to_location,
        airport=airport,
        seats_available=seats_available,
        plane_number=plane_number,
        port_number=port_number,
        fly_code=fly_code,
        date=route_date,
    )
    session.add(new_route)
    session.commit()
    session.refresh(new_route)
    return new_route

def get_all_air_routes(session: Session):
    return session.query(AirRoute).all()

def reserve_flight_route(fly_code: str, session: Session):
    air_route = session.query(AirRoute).filter(
        AirRoute.fly_code == fly_code
    ).first()

    if not air_route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Air route not found"
        )
    
    if air_route.seats_available <= 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Air route not available"
        )
    
    air_route.seats_available -= 1
    session.commit()

def cancel_flight_route(fly_code: str, session: Session):
    air_route = session.query(AirRoute).filter(
        AirRoute.fly_code == fly_code
    ).first()

    if not air_route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Air route not found"
        )
    
    air_route.seats_available += 1
    session.commit()
    