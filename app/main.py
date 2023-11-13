"""Module docstring"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    """function docstring"""
    return {"message": "Hell on World"}


@app.get("/data/{name}")
# pylint: disable=C0303
async def read_data(name: str = "ion"): 
    """function docstring"""
    return {"message": f"Hell on World {name.capitalize()}"}

# def sum_(a: int, b: int) -> int:
#     """mypy check"""
#     return a + b
