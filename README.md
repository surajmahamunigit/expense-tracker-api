# 💰 Expense Tracker API (FastAPI)

A backend REST API built with FastAPI that allows users to register, login, and manage personal expenses securely using JWT authentication.

---

## 🚀 Features

- User Registration & Login
- JWT Authentication (secure token-based auth)
- Password hashing using bcrypt
- Create / Read / Update / Delete Expenses
- Ownership-based access control (users can only access their own data)
- SQLite database with SQLAlchemy ORM

---

## 🧠 Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)

---

## 🔐 Security Features

- JWT token authentication
- Password hashing (bcrypt)
- Protected endpoints using dependencies
- User-level data isolation

---

## 📌 API Endpoints

### Auth
- POST `/register`
- POST `/login`

### Expenses
- POST `/expenses/`
- GET `/expenses/`
- PUT `/expenses/{id}`
- DELETE `/expenses/{id}`

---

## 📂 Project Structure

app/
├── routes/
├── models/
├── schemas/
├── db/
├── utils/

---

## 📚 Key Learnings

- FastAPI backend development
- Authentication & authorization (JWT)
- SQLAlchemy ORM
- Secure API design
- Real-world CRUD architecture