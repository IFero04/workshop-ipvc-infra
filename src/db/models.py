from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class AirRoute(Base):
    __tablename__ = 'air_route'
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_location = Column(String, nullable=False)
    to_location = Column(String, nullable=False)
    airport = Column(String, nullable=False)
    seats_available = Column(Integer, nullable=False)
    plane_number = Column(String, nullable=False)
    port_number = Column(String, nullable=False)
    fly_code = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    def __str__(self):
        return (
            f"AirRoute(id={self.id}, from_location='{self.from_location}', "
            f"to_location='{self.to_location}', airport='{self.airport}', "
            f"seats_available={self.seats_available}, plane_number='{self.plane_number}', "
            f"port_number='{self.port_number}', fly_code='{self.fly_code}', date='{self.date}')"
        )