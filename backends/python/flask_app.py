from flask import Flask, jsonify, request
from logic import average, compute, multiply

app = Flask(__name__)


@app.route("/average", methods=["POST"])
def average_handler():
    data = request.get_json()
    result = average(**data)
    return jsonify({"status": "success", "data": result})


@app.route("/compute", methods=["POST"])
def compute_handler():
    data = request.get_json()
    result = compute(**data)
    return jsonify({"status": "success", "data": result})


@app.route("/multiply", methods=["POST"])
def multiply_handler():
    data = request.get_json()
    result = multiply(**data)
    return jsonify({"status": "success", "data": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
