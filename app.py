from mongo_config import MongoConnection
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
con = MongoConnection()

@app.route("/number-of-submissions")
def number_of_submissions():
  res = con.db.counts.find_one()
  return {'count':res['count']}



