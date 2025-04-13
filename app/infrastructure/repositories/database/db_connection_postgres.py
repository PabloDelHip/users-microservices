from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class PostgresDB:
    def __init__(self):
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', '11223344')
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = os.getenv('DB_PORT', '5432')
        self.database = os.getenv('DB_NAME', 'leadse')

        self._engine = None
        self._SessionLocal = None

    def get_engine(self):
        if not self._engine:
            db_url = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
            self._engine = create_engine(db_url, echo=False)
        return self._engine

    def get_session(self):
        if not self._SessionLocal:
            self._SessionLocal = sessionmaker(bind=self.get_engine(), autoflush=False, autocommit=False)
        return self._SessionLocal()

# Instancia reutilizable
db = PostgresDB()
