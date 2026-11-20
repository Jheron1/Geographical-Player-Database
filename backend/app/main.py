from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db.db import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def get_health():
    return {"status": "OK"}

@app.get("/health-db")
def health_db(db: Session = Depends(get_db)):
    return {"status": "db OK"}