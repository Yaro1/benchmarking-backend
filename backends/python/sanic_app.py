from sanic import Sanic
from sanic.response import json
from logic import average, compute, multiply

app = Sanic("SanicApp")


@app.post("/average")
async def average_handler(request):
    data = request.json
    result = average(**data)
    return json({"status": "success", "data": result})

@app.post("/compute")
async def compute_handler(request):
    data = request.json
    result = compute(**data)
    return json({"status": "success", "data": result})

@app.post("/multiply")
async def multiply_handler(request):
    data = request.json
    result = multiply(**data)
    return json({"status": "success", "data": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)