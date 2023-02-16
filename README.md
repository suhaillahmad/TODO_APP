# TODO_APP

This is a Django based REST API for a simple Todo application. The API allows the user to perform CRUD operations on tasks and mark tasks as complete or incomplete. The backend uses SQLite as its database.

## Installation

1. Clone the repository:

```CMD
git clone https://github.com/suhaillahmad/TODO_APP.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install, Create and activate a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```

Activate the virtual environment

```CMD
source venv/bin/activate
```

3. Install the dependencies:

```CMD
pip install -r requirements.txt
```

4. Run the migrate command

```CMD
python manage.py migrate
```

5. Run the backend server on localhost:

```CMD
python manage.py runserver
```

You can access the endpoints from your web browser following this url

```url
http://127.0.0.1:8000
```

You should now be able to access the API by visiting http://127.0.0.1:8000 in your web browser.

## API Endpoints

| Method   | URL                                         | Description                   |
| -------- | ------------------------------------------- | ----------------------------- |
| `GET`    | `/public_task/task/`                        | Retrieve all task.            |
| `POST`   | `/public_task/task/`                        | Create a new task.            |
| `PATCH`  | `/public_task/task/?task_id=2`              | Update task #2.               |
| `DELETE` | `/public_task/task/?task_id=2`              | Delete task #2.               |
| `PATCH`  | `public_task/task_status_update/?task_id=2` | Update Status of the task #2. |

### Private Task

| Method | URL                       | Description                  |
| ------ | ------------------------- | ---------------------------- |
| `POST` | `/private_task/Register/` | For A New User Resgistration |
| `POST` | `/private_task/login/`    | For Getting the access token |

The Private Task API uses token authentication. To authenticate, include an Authorization header in your requests with the format Token <your_token>. You can obtain a token by sending a POST request to http://127.0.0.1:8000/private_task/login/ with a JSON body containing your username and password.

| Method   | URL                                          | Description                    |
| -------- | -------------------------------------------- | ------------------------------ |
| `GET`    | `/private_task/task/`                        | Retrieve all task of the user. |
| `POST`   | `/private_task/task/`                        | Create a new task.             |
| `PATCH`  | `/private_task/task/?task_id=2`              | Update task #2.                |
| `DELETE` | `/private_task/task/?task_id=2`              | Delete task #2.                |
| `PATCH`  | `private_task/task_status_update/?task_id=2` | Update Status of the task #2.  |

## API Request and Response

`GET /public_task/task/`

```
[
    {
        "id": 1,
        "task": String,
        "is_completed": Bool,
        "time": String
    },
    {
        "id": 2,
        "task": String,
        "is_completed": Bool,
        "time": String
    }
]

```

`POST /public_task/task/`

Request JSON

```
{
    "task":String
}

```

Response

Status Code : 201 Created

```
{
    "id": 3,
    "task": String,
    "is_completed": Bool,
    "time": String
}

```

`PATCH /public_task/task/?task_id=2`

Request JSON

```
{
    "task":String
}

```

Response

Status Code : 200 OK

```
{
    "id": 2,
    "task": String,
    "is_completed": Bool,
    "time": String
}

```

`DELETE /public_task/task/?task_id=2`

Response

Status Code : 204 NO CONTENT

### Registration And Login

`/private_task/Register/`

Resquest JSON

```
{
    "username" : String,
    "password" : String
}

```

Response

Status Code : 201 Created

```

{
    "refresh": String,
    "access": String
}

```

`POST /private_task/login/`

Resquest JSON

```
{
    "username" : String,
    "password" : String
}

```

Response

Status Code : 200 OK

```

{
    "refresh": String,
    "access": String
}

```

The Request and Response for other `Private api` are same as the `Public api` The `Private API Just Uses Token Authentication`

## Docker Commands

```
docker compose run web python manage.py makemigrations
```
```
docker compose run web python manage.py migrate
```
```
docker compose up
```

Hosted Link - `https://TODOAPP-1.suhailahmad4.repl.co`
