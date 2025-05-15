from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(..., example="Abc Kumar Xyz")
    age: int = Field(..., gt=0, example=14)
    grade: str = Field(..., example="8th")

class Student(StudentCreate):
    id: int
