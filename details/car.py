from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/cars")
def home():
    cars = [
        {'id':1, 'name':'BMW'},
        {'id': 2, 'name': 'AUDI'},
        {'id': 3, 'name': 'HONDA'}
    ]
    return jsonify(cars)

if __name__=="__main__":
    app.run(debug=True)