import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    age: int = Field(..., gt=0, le=18)


@app.post('/student', response_model=Student, response_model_exclude={'id'})
def create_stuent(student: Student) -> Student:
    return student


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
