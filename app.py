from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
  return "<h1>Hello World</h1>"

@app.route("/test-route")
def test_route():
  return "<h1>You are in the test route</h1>"

  