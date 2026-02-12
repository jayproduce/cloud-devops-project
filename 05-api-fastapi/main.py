from fastapi import FastAPI, HTTPException

app = FastAPI()

numbers_db = []
current_id = 1


# ➜ Ajouter un nombre
@app.post("/numbers")
def add_number(value: int):
    global current_id
    
    number_entry = {
        "id": current_id,
        "value": value
    }
    
    numbers_db.append(number_entry)
    current_id += 1
    
    return {"message": "Number added", "data": number_entry}


# ➜ Voir tous les nombres
@app.get("/numbers")
def get_numbers():
    return numbers_db


# ➜ Voir un nombre par ID
@app.get("/numbers/{number_id}")
def get_number(number_id: int):
    for number in numbers_db:
        if number["id"] == number_id:
            return number
    raise HTTPException(status_code=404, detail="Number not found")


# ➜ Supprimer un nombre
@app.delete("/numbers/{number_id}")
def delete_number(number_id: int):
    for number in numbers_db:
        if number["id"] == number_id:
            numbers_db.remove(number)
            return {"message": "Number deleted"}
    raise HTTPException(status_code=404, detail="Number not found")





     
          