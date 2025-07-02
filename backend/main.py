from contextlib import asynccontextmanager
from fastapi import Body, Depends, FastAPI, HTTPException, Path
from typing import Optional, List
from sqlmodel import SQLModel, Field, Session, create_engine, select
from fastapi.middleware.cors import CORSMiddleware
import os 
import sqlite3

# Define the Employee model
class Employee(SQLModel, table=True):
    __tablename__ = "employees" # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name:str
    last_name:str
    title:str

# Create the database engine
sqlite_file_name = "employees.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=True) # core database connection object that the app will use for all database operations

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creat tables at startup
    SQLModel.metadata.create_all(engine)
    yield
    # (Optional) Cleanup code here

app = FastAPI(lifespan=lifespan)

# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
# Create an employee
@app.post("/api/employees", response_model=Employee)
def create_employee(employee: Employee, session: Session = Depends(get_session)):
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee

# Get all employees
@app.get("/api/employees", response_model=List[Employee])
def get_employees(session: Session = Depends(get_session)):
    employees = session.exec(select(Employee)).all()
    return employees

# Get one employee
@app.get("/api/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int = Path(...), session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# delete employee
@app.delete("/api/employees/{employee_id}")
def delete_employee(employee_id: int = Path(...), session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    session.delete(employee)
    session.commit()
    return {"ok": True}

# update employee
@app.put('/api/employees/{employee_id}', response_model=Employee)
def update_employee(
    employee_id: int = Path(...),
    updated: Employee = Body(...),
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    # update fields
    employee.first_name = updated.first_name
    employee.last_name = updated.last_name
    employee.title = updated.title
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee


