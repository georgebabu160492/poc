# Intro

- This web application was created to demonstrate a cutting-edge full stack development toolset and useage of industry best practices and patterns. It uses PostgreSQL as the database, FastAPI as the web framework, SQLAlchemy as the database ORM, ReactJS as the UI, Docker as the containerization tool and it leverages Swagger to document APIs.
- This application demonstrates a simple Create, Read, Update, and Delete (CRUD) functionality for project allocation.

# Application Architecture

- Backend

The execution starts from the `backend/main.py` file and loads sample data for the first time. The event will get triggered when there is a new project allocation entry and it will be saved inside `ActivityLog` model.

The application contains the following endpoints:

1. /health-check (GET method) - returns success message if backend is working correctly
2. /api/project (GET method) - to list all project allocations
3. /api/project (POST method) - to create a projects allocations
4. /api/project/{id} (PUT method) - to update a projects allocations
5. /api/project/{id} (DELETE method) - to delete a projects allocations
6. /get_form_iniital_data (GET method) - to get all required datas for above APIs to work properly

Refer to `Swagger documentation` for details at `http://127.0.0.1:8000/docs#/`

Command to run this application locally using docker is `docker-compose up --build`.

NOTE - It will take sometime to complete the build creation.

- Frontend

The application uses the APIs mentioned above for creating, listing, editing and deleting the data. Exception handlers around APIs to handle any errors that may occur are also implemented.


# About the developer

George Babu is a full stack developer with extensive experience with multiple development tools and frameworks.
