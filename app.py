from flask import Flask
from flask_cors import CORS
from db_interaction import DBInteraction

app = Flask(__name__)
CORS(app)
dbi = DBInteraction()

@app.route("/number-of-submissions")
def number_of_submissions():
  count = dbi.get_submissions_count("seta-est.cvcpj1fhj3k9.us-east-2.rds.amazonaws.com", "est")
  return {"count": count}

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)