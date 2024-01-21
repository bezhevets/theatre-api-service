# Theatre Service API Service

Theatre API Service is a Django-based RESTful API for managing plays, performances, actors and more. It provides endpoints for creating, updating, and retrieving thatre-related data, as well as user registration and order management.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation Git](#installation)
- [Run with Docker](#run-with-docker)

## Introduction

Theatre API Service is designed to streamline the management of theatre-related data and user interactions. Whether you're developing an app for theatre, building a play reservation system, or just exploring Django REST APIs, this project provides a solid foundation.

### Features:
- JWT Authentication
- Email-Based Authentication
- Pagination for all pages
- API documentation
- CRUD operations for performances, plays, actors, genres, theatre halls and orders.
- Add images for plays
- Managing reservations and tickets

## Installation

1. Clone the repository:

   ```
   https://github.com/bezhevets/theatre-api-service.git
   ```
2. Create .env file and define environmental variables following .env.example:
   ```
   POSTGRES_HOST= your db host
   POSTGRES_DB= name of your db
   POSTGRES_USER= username of your db user
   POSTGRES_PASSWORD= your db password
   SECRET_key=" your django secret key "
   ```
3. Create a virtual environment::
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:

   - On macOS and Linux:
   ```source venv/bin/activate```
   - On Windows:
   ```venv\Scripts\activate```
5. Install project dependencie:
   ```
    pip install -r requirements.txt
   ```
6. Run database migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
   
## Run with Docker
Docker should be installed.

1. Pull docker container:

   ```
   docker pull ke1erman/theatre-api-service
   ```
2. Rull docker container
   ```
    docker-compose build
    docker-compose up
   ```
   
