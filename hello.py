import json

from flask import Flask, request, jsonify, redirect, current_app
from functools import wraps

from shaolin import Shaolin

app = Flask(__name__)
s = Shaolin()

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function

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
@support_jsonp
def password():
    return jsonify(password=s.generate_password())

if __name__ == "__main__":
    app.debug = True
    app.run()
