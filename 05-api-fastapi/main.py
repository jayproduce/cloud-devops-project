from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal

# ➜ Crée la table dans la base
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ➜ Dépendance pour ouvrir/fermer la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ➜ CREATE
@app.post("/numbers")
def create_number(value: int, db: Session = Depends(get_db)):
    db_number = models.Number(value=value)
    db.add(db_number)
    db.commit()
    db.refresh(db_number)
    return db_number


# ➜ READ ALL
@app.get("/numbers")
def get_numbers(db: Session = Depends(get_db)):
    return db.query(models.Number).all()


# ➜ READ ONE
@app.get("/numbers/{number_id}")
def get_number(number_id: int, db: Session = Depends(get_db)):
    number = db.query(models.Number).filter(models.Number.id == number_id).first()
    if not number:
        raise HTTPException(status_code=404, detail="Number not found")
    return number


# ➜ DELETE
@app.delete("/numbers/{number_id}")
def delete_number(number_id: int, db: Session = Depends(get_db)):
    number = db.query(models.Number).filter(models.Number.id == number_id).first()
    if not number:
        raise HTTPException(status_code=404, detail="Number not found")
    
    db.delete(number)
    db.commit()
    return {"message": "Deleted successfully"}

@app.put("/numbers/{number_id}")
def update_number(number_id: int, updated_data: NumberUpdate, db: Session = Depends(get_db)):
    number = db.query(models.Number).filter(models.Number.id == number_id).first()
    if not number:
        raise(HTTPException(status_code= 404, detail= "Number not found"))
    number.value =  updated_data.value
    db.commit()
    db.refresh(number)
    return{"message":"number update successfully"}

@app.get("/numbers/filter/{min_value}")
def get_number(min_value : int, db: Session = Depends(get_db)):
    number = db.query(models.Number).filter(models.Number.value >= min_value).all()
    return numbers 

@app.get("/numbers/count")
def count_numbers(db: Session = Depends(get_db)):
    total = db.query(func.count(models.Number.id)).scalar()
    return {"count": total}

@app.delete("/numbers")
def delete_allnumbers(db: Session = Depends(get_db)):
    db.query(models.Number).delete()
    db.commit()
    return {"message": "All numbers deleted"}

@app.get("/numbers/count")
def coount_number(db: Session = Depends(get_db)):
    total = db.query(func.count(models.Number.id)).scalar()
    return {"count": total}

@app.delete("/numbers")
def delete_number(db: Session = Depends(get_db)):
    db.query(models.Number).delete()
    db.commit()
   




  



     
          