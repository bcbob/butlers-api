from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Branch
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Butler's Pizza API is alive!"}

@app.get("/branches")
def get_branches(db: Session = Depends(get_db)):
    branches = db.query(Branch).all()
    return branches