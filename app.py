from flask import Flask
from flask_cors import CORS
from db_interaction import DBInteraction
from record_count import RecordCount

app = Flask(__name__)
CORS(app)
dbi = DBInteraction()
rc = RecordCount()

@app.route("/number-of-submissions")
def number_of_submissions():
  count = rc.counts
  return {"count": count}

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)

rc.increment_count()
