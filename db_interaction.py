import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd

class DBInteraction:

  def __init__(self):
    self.username = "seta"
    self.password = "defaultUnsafePassword"

  def get_submissions_count(self, host, database):
    conn = pg.connect(
      host=host,
      database=database,
      user=self.username,
      password=self.password)

    cur = conn.cursor()
    cur.execute("select count (*) from responses;")
    res = cur.fetchone()
    return res[0]

