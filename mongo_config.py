import pymongo

class MongoConnection:
  def __init__(self):
    self.client = pymongo.MongoClient("mongodb+srv://bernard:GdpGCrjGfYyoFEdi@cluster0.xylne.mongodb.net/?retryWrites=true&w=majority")
    self.db = self.client.PisaDataWarehouse
    self.counts = self.db.counts
  


