import psycopg2
from psycopg2.extras import RealDictCursor #to make cursor for PostgreSQL we need this

from config import Config

class BrandRepositoryPostgreSQL:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )