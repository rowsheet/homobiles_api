from flask import Flask, request, jsonify
import json
import os
import requests
import sys
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    print("test print", file=sys.stdout)
    sys.stdout.write("test print with flush\n")
    sys.stdout.flush()
    return "test return"

@app.route('/ping', methods=['POST', 'GET'])
def ping():
    print("got ping")
    return "pong"

if __name__ == '__main__':
    app.run(
        host= '0.0.0.0',
        port=9999,
        debug=True
    )
