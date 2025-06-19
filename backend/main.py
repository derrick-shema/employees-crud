from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
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
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=True)

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

@app.get("/api/employees", response_model=List[Employee])
def get_employees(session: Session = Depends(get_session)):
    employees = session.exec(select(Employee)).all()
    return employees
