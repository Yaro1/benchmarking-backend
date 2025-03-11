import uvicorn
from logic import average, compute, multiply
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse

app = Starlette()


@app.route("/average", methods=["POST"])
async def average_handler(request: Request):
    data = await request.json()
    result = average(**data)
    return JSONResponse({"status": "success", "data": result})


@app.route("/compute", methods=["POST"])
async def compute_handler(request: Request):
    data = await request.json()
    result = compute(**data)
    return JSONResponse({"status": "success", "data": result})


@app.route("/multiply", methods=["POST"])
async def multiply_handler(request: Request):
    data = await request.json()
    result = multiply(**data)
    return JSONResponse({"status": "success", "data": result})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
