from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .routers import auth, employees

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management System", version="1.0.0")

app.include_router(auth.router)
app.include_router(employees.router)

@app.get("/")
def root():
    return {"message": "Employee Management System is running"}

@app.get("/health")
def health():
    db = next(get_db())
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    finally:
        db.close()

@app.get("/metrics")
def metrics(db: Session = next(iter([get_db()]))):
    return {"service": "employee-management", "status": "running"}
