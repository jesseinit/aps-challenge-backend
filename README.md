# APS-Challenge Backend

## Installing

```sh
    // Setup Project
    $ git clone git@github.com:jesseinit/aps-challenge-backend.git
    $ cd aps-challenge-backend
    $ git checkout main

    // Activate Virtual Ennvironment
    $ python -m venv venv
    $ source venv/bin/acivate

    // Install application dependencies
    $ pip install -r requirement.txt

    // Setup Database and Run Migrations
    $ make migrate
    OR
    $ python manage.py makemigrations && python manage.py migrate
```

## Running the application

Run the command below to run the application locally.

```
  $ make dev
  OR
  $ python manage.py runserver
```

## Documentation

API Routes Documentation can be found [here](https://documenter.getpostman.com/view/7875106/TzJvfcmv)

## Built With

The project has been built with the following technologies so far:

- [Django](https://www.djangoproject.com/) - web framework for building websites using Python
- [Django Rest Framework](https://www.django-rest-framework.org) - is a powerful and flexible toolkit for building Web APIs.
- [PostgreSQL](https://www.postgresql.org/) - A production-ready relational database system emphasizing extensibility and technical standards compliance.
- [SQLite](https://www.postgresql.org/) - Database management system used to persists the application's data.
