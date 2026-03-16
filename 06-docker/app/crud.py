from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models


def create_number(db: Session, value: int):
    db_number = models.Number(value=value)
    db.add(db_number)
    db.commit()
    db.refresh(db_number)
    return db_number


def get_numbers(db: Session):
    return db.query(models.Number).all()


def get_number(db: Session, number_id: int):
    return db.query(models.Number).filter(
        models.Number.id == number_id
    ).first()


def update_number(db: Session, number_id: int, value: int):
    number = get_number(db, number_id)
    if number:
        number.value = value
        db.commit()
        db.refresh(number)
    return number


def delete_number(db: Session, number_id: int):
    number = get_number(db, number_id)
    if number:
        db.delete(number)
        db.commit()
    return number


def count_numbers(db: Session):
    return db.query(func.count(models.Number.id)).scalar()
