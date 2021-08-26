# fastapi-async-sqlmodel

This repository is a simple tutorial to easily setup a FastAPI application with SQLModel using Async SQLAlchemy sessions.

## Requirements

- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

```sh
git clone git@github.com:Cedric-Magnan/fastapi-async-sqlmodel.git
cd fastapi-async-sqlmodel
poetry install
```

## Local Deployment

```sh
export SQLITE_FILE_DB_PATH="/path/to/your/sqlite/db/file.db"
uvicorn app:app
```
