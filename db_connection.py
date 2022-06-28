import psycopg2 as pg
from sqlalchemy import create_engine

def getNumberOfSubmissions():
  conn = pg.connect(
    host="seta-fin.cvcpj1fhj3k9.us-east-2.rds.amazonaws.com",
    database="fin",
    user="seta",
    password="defaultUnsafePassword")

  cur = conn.cursor()
  res = cur.execute("SELECT * FROM responses;")
  

