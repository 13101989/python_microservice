from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hell on World"}

@app.get("/data/{name}")
async def read_data(name: str = "ion"):
    return {"message": f"Hell on World {name}"}