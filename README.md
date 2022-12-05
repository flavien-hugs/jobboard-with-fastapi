# JobBoard API

## Technology Stack:

- Python 3.10+
- pipenv ou pip
- Pytest
- sqlalchemy
- Alembic
- Postgresql

## Clone the project

```
git clone https://github.com/flavienn-hugs/jobboard-with-fastapi.git
```

## Test the project locally

```
run: make runserver
or
uvicorn backend.main:app --reload
```

## Installing the dependencies

```
If use pipenv: pipenv install

or

If using pip: pip install -r backend/requirements.txt
```

## Features

- List a job post
- Details of the job post
- Create a job post
- Update the job
- Delete the job
- Permissions (Authorization required, only superuser and the original author can delete)
- Authentication ( Registration and Login )
- Test our Endpoints
- Test Coverage
- Webapp for Jobboard
