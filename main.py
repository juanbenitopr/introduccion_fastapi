from typing import List

import uvicorn
from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    age: int = Field(..., gt=0, le=18)


@app.post('/student', response_model=Student, response_model_exclude={'id'})
def create_stuent(student: Student) -> Student:
    return student


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
def list_students(student_filter: StudentFilter = Depends()) -> List[Student]:
    students = [
        Student(id=1, name='Juan', age=3),
        Student(id=2, name='Antonio', age=10),
        Student(id=3, name='Alberto', age=12),
    ]
    return [student for student in students if StudentFilter(age=student.age, name=student.name) == student_filter]


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
