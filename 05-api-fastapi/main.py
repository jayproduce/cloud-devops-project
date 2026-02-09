from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API DevOps active"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/add")
def add (a: int, b: int):
    return {"result": a + b}
