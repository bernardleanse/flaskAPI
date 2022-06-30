import os
import pymongo

class MongoConnection:
  def __init__(self):
    self.client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
    self.db = self.client.PisaDataWarehouse
    self.counts = self.db.counts
  


