# FastAPI To-Do API

A simple CRUD API built with FastAPI.

## Features
- Create tasks
- Read tasks
- Update tasks (PATCH)
- Delete tasks

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints

- GET /
- POST /items
- GET /items
- GET /items/{item_id}
- DELETE /items/{item_id}
- PATCH /items/{item_id}