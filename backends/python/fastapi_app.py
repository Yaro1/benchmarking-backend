from fastapi import FastAPI, Request
from logic import average, compute, multiply

app = FastAPI()


@app.post("/average")
async def average_handler(request: Request):
    data = await request.json()
    result = average(**data)
    return {"status": "success", "data": result}


@app.post("/compute")
async def compute_handler(request: Request):
    data = await request.json()
    result = compute(**data)
    return {"status": "success", "data": result}


@app.post("/multiply")
async def multiply_handler(request: Request):
    data = await request.json()
    result = multiply(**data)
    return {"status": "success", "data": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
