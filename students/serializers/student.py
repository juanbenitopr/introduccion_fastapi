from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str
    age: int = Field(..., gt=0, le=18)

    class Config:
        orm_mode = True
