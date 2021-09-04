from time import time
from typing import List

import uvicorn
from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel, Field
from starlette.requests import Request

from db import Session, get_session, Base, engine
from models.student import StudentSQL

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int = Field(..., gt=0, le=18)

    class Config:
        orm_mode = True


@app.post('/student', response_model=Student)
def create_stuent(student: Student, session: Session = Depends(get_session)) -> Student:
    student_sql = StudentSQL(name=student.name, age=student.age)

    session.add(student_sql)

    raise Exception('test')

    return Student.from_orm(student_sql)


def get_student_name(name: str) -> str:
    return name


class StudentFilter:

    def __init__(self, age: int, name: str = Depends(get_student_name)):
        self.age = age
        self.name = name

    def __eq__(self, other: 'StudentFilter') -> bool:
        return self.age == other.age or self.name == other.name


def validate_request(token: str = Header(...)):
    if token != 'Bearer':
        raise HTTPException(status_code=401, detail='Token Invalid')


@app.get('/student', response_model=List[Student], dependencies=[Depends(validate_request)])
def list_students(student_filter: StudentFilter = Depends(), session: Session = Depends(get_session)) -> List[Student]:
    students: List[StudentSQL] = session.query(StudentSQL).filter_by(name=student_filter.name, age=student_filter.age)

    return [Student.from_orm(student) for student in students]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
