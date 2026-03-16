from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/numbers", response_model=schemas.NumberResponse)
def create(number: schemas.NumberCreate, db: Session = Depends(get_db)):
    return crud.create_number(db, number.value)


@app.get("/numbers", response_model=list[schemas.NumberResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_numbers(db)


@app.get("/numbers/{number_id}", response_model=schemas.NumberResponse)
def read_one(number_id: int, db: Session = Depends(get_db)):
    number = crud.get_number(db, number_id)
    if not number:
        raise HTTPException(status_code=404, detail="Not found")
    return number


@app.put("/numbers/{number_id}", response_model=schemas.NumberResponse)
def update(number_id: int, data: schemas.NumberUpdate, db: Session = Depends(get_db)):
    number = crud.update_number(db, number_id, data.value)
    if not number:
        raise HTTPException(status_code=404, detail="Not found")
    return number


@app.delete("/numbers/{number_id}")
def delete(number_id: int, db: Session = Depends(get_db)):
    number = crud.delete_number(db, number_id)
    if not number:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted"}

  



     
          