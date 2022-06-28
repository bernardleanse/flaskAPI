from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/number-of-submissions")
def hello_world():
  return "<h1>Hello World</h1>"