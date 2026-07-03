# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to manage a simple todo list. Students will learn how to design endpoints, validate requests with Pydantic, and run a local development server.

## 📝 Tasks

### 🛠️	Create a CRUD API for Todos

#### Description
Implement a RESTful API that supports create, read, update, and delete operations for todo items.

#### Requirements
Completed program should:

- Provide endpoints: `GET /todos`, `GET /todos/{id}`, `POST /todos`, `PUT /todos/{id}`, `DELETE /todos/{id}`
- Use Pydantic models for request and response validation
- Store data in-memory (list or dict); no external database required
- Return appropriate HTTP status codes (201 for creation, 404 when not found)
- Include example `curl` commands to test the API


### 🛠️	Add input validation and run instructions

#### Description
Add input validation for request fields and include instructions for running the server locally.

#### Requirements
Completed program should:

- Validate fields (e.g., non-empty `title`, `completed` is boolean)
- Provide example `curl` requests demonstrating each endpoint
- Include a short run command using `uvicorn` (development mode)


----

Starter code is provided in `starter-code.py`. Install dependencies with `pip install -r requirements.txt` and run the app with:

```
uvicorn starter-code:app --reload
```
