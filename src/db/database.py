from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


class SQLite:
    def __init__(self, database_url):
        self._engine = None
        self._SessionLocal = None
        self.create_connection(database_url)
    
    def __enter__(self):
        self._session = self._SessionLocal()
        return self._session
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._session.close()
    
    def create_connection(self, database_url):
        self._engine = create_engine(database_url, echo=False)
        self._SessionLocal = sessionmaker(bind=self._engine)
        self.create_tables()

    def create_tables(self):
        Base.metadata.create_all(bind=self._engine) 
