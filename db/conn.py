from utils.config import Config
from psycopg2 import connect


def connect_to_db():
    # Conexión a la base de datos
    conn = connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASS
    )

    return conn
