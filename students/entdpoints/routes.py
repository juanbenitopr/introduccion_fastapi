from typing import List

from fastapi import APIRouter

from students.entdpoints.student_api import StudentAPI
from students.serializers.student import Student

router = APIRouter()

student_api = StudentAPI()

router.add_api_route('', endpoint=student_api.create, response_model=Student, methods=['POST'])
router.add_api_route('', endpoint=student_api.read, response_model=List[Student], methods=['GET'])
