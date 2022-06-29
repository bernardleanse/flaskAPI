import psycopg2
from db_connections import DatabaseConnections
from flask import Flask
from flask_cors import CORS
from db_interaction import DBInteraction
from record_count import RecordCount

app = Flask(__name__)
CORS(app)
db_cons = DatabaseConnections()
db_cons.set_up_connections() 
rc = RecordCount()

@app.route("/number-of-submissions")
def number_of_submissions():
  counts = [get_quantity_of_records(con) for con in db_cons.connections.values()]
  return {"count": sum(counts)}

def get_quantity_of_records(connection):
  cursor = connection.cursor()
  cursor.execute("select count (*) from responses;")
  quant = cursor.fetchone()[0]
  cursor.close()
  return quant

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)