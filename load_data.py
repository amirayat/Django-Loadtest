import os
import json
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))

con = psycopg2.connect(
    dbname='postgres',
    user=DB_USER, 
    host=DB_HOST,
    password=DB_PASSWORD
    )

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = con.cursor()

cur.execute(
    sql.SQL("DROP DATABASE IF EXISTS {}").format(
        sql.Identifier(DB_NAME))
    )

cur.execute(
    sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(DB_NAME))
    )

con = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER, 
    host=DB_HOST,
    password=DB_PASSWORD
    )

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = con.cursor()

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.management import call_command
from countries.models import Country
from pathlib import Path

call_command('migrate')

BASE_DIR = str(Path(__file__).resolve().parent)

COUNTRIES_PATH = BASE_DIR + '/db_data/countries.json'

def insert_countries():
    with open(COUNTRIES_PATH) as fp:
        data = json.load(fp)
        feed_list = [Country(**item) for item in data]
        Country.objects.bulk_create(feed_list)

insert_countries()

