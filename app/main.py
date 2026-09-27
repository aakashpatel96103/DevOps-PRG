from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .routers import auth, employees

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management System",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(employees.router)


@app.get("/")
def root():
    return {
        "message": "Employee Management System is running"
    }


@app.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }


@app.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    employee_count = db.execute(
        text("SELECT COUNT(*) FROM employees")
    ).scalar()

    return {
        "service": "employee-management",
        "status": "running",
        "employees": employee_count
    }
