from fastapi import FastAPI

app = FastAPI()

numbers_db = []

@app.post("/numbers")
def stock_numbers(number : int):
    numbers_db.append(number)
    return "message": {"number added successfully"}

@app.get("/numbers")
def get_numbers():
    return numbers_db




     
          