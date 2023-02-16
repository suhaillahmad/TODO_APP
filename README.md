# TODO_APP

This is a Django based REST API for a simple Todo application. The API allows the user to perform CRUD operations on tasks and mark tasks as complete or incomplete. The backend uses SQLite as its database.

## Installation

Clone the main branch and run the following command:

```CMD
docker compose up --build
```

You should now be able to access the API by visiting http://0.0.0.0:8000/ in your web browser.

## API Endpoints

| Method   | URL                                         | Description                              |
| -------- | ----------------------------------------    | ---------------------------------------- |
| `GET`    | `/public_task/task/`                        | Retrieve all task.                       |
| `POST`   | `/public_task/task/`                        | Create a new task.                       |
| `PATCH`  | `/public_task/task/?task_id=2`              | Update task #2.                          |
| `DELETE` | `/public_task/task/?task_id=2`              | Delete task #2.                          |
| `PATCH`  | `public_task/task_status_update/?task_id=2` | Update Status of the task #2.            |
