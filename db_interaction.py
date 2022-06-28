from socket import TCP_NOTSENT_LOWAT
import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd
import json

class DBInteraction:

  def __init__(self):
    self.username = "seta"
    self.password = "defaultUnsafePassword"
    self.databases = json.load(open("databases.json"))

  def get_submissions_count(self, **kwargs):
    conn = pg.connect(
      host=kwargs['host'],
      database=kwargs['database'],
      user=self.username,
      password=self.password)
    cur = conn.cursor()
    cur.execute("select count (*) from responses;")
    res = cur.fetchone()
    cur.close()
    conn.close()
    return res[0]

  def get_total_submission_count(self):
    total = 0
    for country_code, url in self.databases.items():
      total += self.get_submissions_count(database=country_code, host=url)
    return total