# 🚀 Flask REST API - User Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST_API-black?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A lightweight and efficient **RESTful API** built using **Flask** that performs complete **CRUD (Create, Read, Update, Delete)** operations for managing user data.

This project was developed as part of an internship assessment to demonstrate understanding of REST API development, HTTP methods, JSON handling, and backend application development using Python and Flask.

---

# 📖 Table of Contents

- Project Overview
- Features
- Tech Stack
- Project Structure
- Installation
- Running the Application
- API Endpoints
- Request & Response Examples
- HTTP Status Codes
- Testing with Postman
- Error Handling
- Future Improvements
- Learning Outcomes
- Author

---

# 📌 Project Overview

REST (Representational State Transfer) APIs are widely used for communication between client applications and backend services.

This project implements a simple **User Management API** that allows clients to:

- View all users
- View a specific user
- Create new users
- Update existing users
- Delete users

The application exchanges data using the **JSON** format and follows standard REST API practices.

---

# ✨ Features

- RESTful API Design
- CRUD Operations
- JSON Request & Response
- Persistent User Storage
- UUID-based User IDs
- Input Validation
- Proper HTTP Status Codes
- Clean Project Structure
- Easy to Test with Postman
- Beginner-Friendly Codebase

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Web Framework |
| JSON | Data Storage |
| Postman | API Testing |

---

# 📂 Project Structure

```
Flask-REST-API/
│
├── app.py
├── users.json
├── requirements.txt
├── README.md
├── Postman_Collection.json
└── .gitignore
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone https://github.com/amritaruhela/flask-rest-api.git
```

---

## Navigate to the Project

```bash
cd flask-rest-api
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Start the Flask development server:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

# 📡 API Endpoints

## Get API Information

| Method | Endpoint |
|---------|----------|
| GET | / |

---

## Get All Users

| Method | Endpoint |
|---------|----------|
| GET | /users |

---

## Get User by ID

| Method | Endpoint |
|---------|----------|
| GET | /users/<id> |

---

## Create User

| Method | Endpoint |
|---------|----------|
| POST | /users |

---

## Update User

| Method | Endpoint |
|---------|----------|
| PUT | /users/<id> |

---

## Delete User

| Method | Endpoint |
|---------|----------|
| DELETE | /users/<id> |

---

# 📤 Sample Request

```json
{
    "name": "Amrita Ruhela",
    "email": "amrita@example.com",
    "age": 21
}
```

---

# 📥 Sample Response

```json
{
    "message": "User created successfully",
    "user": {
        "id": "5d1f2d6d-1b4d-4e87-a17f-78c43f73d5d5",
        "name": "Amrita Ruhela",
        "email": "amrita@example.com",
        "age": 21
    }
}
```

---

# 📊 HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# 🧪 Testing with Postman

The repository includes a Postman collection.

Steps:

1. Open Postman
2. Import **Postman_Collection.json**
3. Start the Flask server
4. Test every endpoint

You can also use **cURL** for testing.

Example:

```bash
curl http://127.0.0.1:5000/users
```

---

# ⚠ Error Handling

The application handles common scenarios including:

- Missing JSON body
- Invalid user ID
- User not found
- Missing required fields
- Invalid HTTP requests

All errors are returned in JSON format with appropriate HTTP status codes.

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- REST APIs
- Flask Framework
- CRUD Operations
- HTTP Methods
- JSON Handling
- Backend Development
- API Testing using Postman
- Basic Software Design Principles

---

# 🚀 Future Improvements

Possible enhancements include:

- SQLite/MySQL Database Integration
- JWT Authentication
- User Login & Registration
- Password Hashing
- Search & Pagination
- API Documentation using Swagger
- Docker Support
- Unit Testing with PyTest
- Deployment on Render or Railway

---

# 👨‍💻 Author

**Amrita Ruhela**

B.Tech Computer Science Engineering (Data Science & Machine Learning)

GitHub: https://github.com/amritaruhela

---

# 📜 License

This project was developed for educational purposes and internship assessment.

Feel free to use and modify it for learning.

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
