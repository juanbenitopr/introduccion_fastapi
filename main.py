from typing import List

import uvicorn
from fastapi import FastAPI, Depends
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


@app.get('/student', response_model=List[Student])
def list_students(name: str = Depends(get_student_name)) -> List[Student]:
    students = [
        Student(id=1, name='Juan', age=3),
        Student(id=2, name='Antonio', age=10),
        Student(id=3, name='Alberto', age=12),
    ]
    return [student for student in students if student.name == name]


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
