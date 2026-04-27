# Expense Tracker API

A REST API for tracking personal expenses built with Python and FastAPI.

## Features
- User registration and login with JWT authentication
- Each user can only access their own expenses
- Full CRUD operations (Create, Read, Update, Delete)
- SQLite database

## Tech Stack
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication (python-jose)
- Argon2 password hashing

## How to Run

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `uvicorn app.main:app --reload`
6. Open: `http://127.0.0.1:8000/docs`

## API Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /register | Create an account | No |
| POST | /login | Get access token | No |
| GET | /expenses | Get all your expenses | Yes |
| POST | /expenses | Add an expense | Yes |
| PUT | /expenses/{id} | Update an expense | Yes |
| DELETE | /expenses/{id} | Delete an expense | Yes |