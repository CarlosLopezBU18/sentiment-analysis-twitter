import sqlite3 as sqlt
from config import DBConfig

sqlt.connect(DBConfig.DB_PATH)
