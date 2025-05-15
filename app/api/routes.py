from fastapi import APIRouter, HTTPException
from typing import List

from app.models.student import Student, StudentCreate

router = APIRouter()

# In-memory database and ID counter
students_db = {}
student_id_counter = 1

@router.get("/")
def root():
    return {"message": "Student Registry API is up and running!"}

@router.get("/students", response_model=List[Student])
def list_students():
    return list(students_db.values())

@router.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    global student_id_counter
    student_data = Student(id=student_id_counter, **student.dict())
    students_db[student_id_counter] = student_data
    student_id_counter += 1
    return student_data

@router.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
