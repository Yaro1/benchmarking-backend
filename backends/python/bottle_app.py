from bottle import Bottle, request, response
from logic import average, compute, multiply

app = Bottle()


@app.post("/average")
def average_handler():
    data = request.json
    result = average(**data)
    return {"status": "success", "data": result}


@app.post("/compute")
def compute_handler():
    data = request.json
    result = compute(**data)
    return {"status": "success", "data": result}


@app.post("/multiply")
def multiply_handler():
    data = request.json
    result = multiply(**data)
    return {"status": "success", "data": result}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
