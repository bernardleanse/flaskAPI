from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/number-of-submissions")
def number_of_submissions():
  return {"count": getNumberOfSubmissions()}

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)