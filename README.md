# Intro

- This online application was created to demonstrate a cutting-edge full stack development tool. It uses  PostgreSQL as the database, FastAPI as the web framework, SQLAlchemy as the database ORM, ReactJS as the UI, Docker as the containerization tool and it leverages Swagger to document APIs.
- A web application created to track and manage applications, it demonstrates Create, Read, Update, and Delete (CRUD) functionalities.

# Application Architecture

- Backend

This application makes use of some sample jsons for its CRUD operations and it is saved inside the backend directory(`/backend/sample_data/`). The execution starts from the `backend/main.py` file.

The application contains the following endpoints

1. /health-check (GET method) - returns success message if backend is working correctly
2. /api/project (GET method) - to list all products
3. /api/project (POST method) - to create a product
4. /api/project/{id} (PUT method) - to update a product
5. /api/project/{id} (DELETE method) - to delete a product
6. /get_form_iniital_data (GET method) - to get all required datas for above APIs to work properly

Refer to `Swagger documentation` for details at `http://127.0.0.1:8000/docs#/`

- Frontend

The application uses the APIs mentioned above for creating, listing, editing and deleting the data. Exception handlers around APIs to handle any errors that may occur are also implemented.


# About the developer

George Babu is a full stack developer with extensive experience with multiple development tools and frameworks.
