import os
import psycopg2cffi
import psycopg2cffi.extras
from dotenv import load_dotenv


load_dotenv()


DB_NAME = os.getenv('DB_NAME')
DB_TABLE = os.getenv('DB_TABLE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))


conn = psycopg2cffi.connect(f"dbname='{DB_NAME}' user='{DB_USER}' host='{DB_HOST}' password='{DB_PASSWORD}'")


def get_countries():
    """
    get all world countries using psycopg cursor 
    """
    cur = conn.cursor(cursor_factory = psycopg2cffi.extras.RealDictCursor)
    cur.execute(f"""SELECT * FROM {DB_TABLE}""")
    countries = cur.fetchall()
    return countries


