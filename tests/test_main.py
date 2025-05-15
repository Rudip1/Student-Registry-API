from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Student Registry API is up and running!"}

def test_add_student():
    payload = {
        "name": "Test User",
        "age": 20,
        "grade": "10"
    }
    response = client.post("/api/students", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert data["age"] == 20
    assert data["grade"] == "10"
    assert "id" in data

def test_get_student():
    # Add a new student first
    new_student = {
        "name": "Retrieve Test",
        "age": 15,
        "grade": "9"
    }
    post_response = client.post("/api/students", json=new_student)
    student_id = post_response.json()["id"]

    # Retrieve that student
    get_response = client.get(f"/api/students/{student_id}")
    assert get_response.status_code == 200
    student_data = get_response.json()
    assert student_data["name"] == "Retrieve Test"
    assert student_data["id"] == student_id

def test_list_students():
    response = client.get("/api/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_student():
    # Add a new student
    new_student = {
        "name": "To Be Deleted",
        "age": 12,
        "grade": "7"
    }
    post_response = client.post("/api/students", json=new_student)
    student_id = post_response.json()["id"]

    # Delete student
    delete_response = client.delete(f"/api/students/{student_id}")
    assert delete_response.status_code == 204

    # Confirm deletion
    get_response = client.get(f"/api/students/{student_id}")
    assert get_response.status_code == 404
