from typing import List

from fastapi import Depends

from students.db import get_session, Session
from students.models.student import StudentSQL
from students.serializers.student import Student


class StudentFilter:

    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name


class StudentAPI:

    def create(self, student: Student, session: Session = Depends(get_session)) -> Student:
        student_sql = StudentSQL(name=student.name, age=student.age)

        session.add(student_sql)

        return Student.from_orm(student_sql)

    def read(self, student_filter: StudentFilter = Depends(), session: Session = Depends(get_session)) -> List[Student]:
        students: List[StudentSQL] = session.query(StudentSQL).filter_by(name=student_filter.name,
                                                                         age=student_filter.age)
        return [Student.from_orm(student) for student in students]
