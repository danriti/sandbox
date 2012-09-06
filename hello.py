import json

from flask import Flask, request, jsonify

from shaolin import Shaolin

app = Flask(__name__)
s = Shaolin()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return request.remote_addr

@app.route("/json", methods=['POST'])
def json():
    if request.method == 'POST':
        return jsonify(request.json)

@app.route("/get/password")
def password():
    d = {'password' : s.generate_password()}
    return jsonify(d)

if __name__ == "__main__":
    app.debug = True
    app.run()
