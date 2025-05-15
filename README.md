#Author
Pravin Oli
pravin.oli.08@gmail.com
olipravin18@gmail.com

# Student Registry API
---
A simple yet functional FastAPI-based microservice that manages student records. This project follows the 12-Factor App principles and is built for easy deployment, testing, and scalability using Docker.

---

#Features

- CRUD API for managing student data (name, age, grade)
- FastAPI for high-performance async APIs
- In-memory database (can be extended to Redis/PostgreSQL)
- Pytest-based unit test
- Docker + Docker Compose setup
- Environment config via `.env`
- Pre-commit hooks for clean code
- CI-ready structure (GitHub Actions friendly)

---

#Requirements

- Python 3.8+
- pip (or pipenv/poetry)
- Docker + Docker Compose (optional)
- Git

---

#Setup

1. Clone the repo

git clone https://github.com/yourusername/student_registry_api.git
cd student_registry_api

2. Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
uvicorn app.main:app --reload

5. open in your browser
http://127.0.0.1:8000/docs

---
#Running Tests
pytest

---
#Video link




