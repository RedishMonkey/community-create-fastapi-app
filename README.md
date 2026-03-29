# Community Create FastAPI App

A simple FastAPI backend application skeleton to start a FastAPI project.
(this is a hobby project any suggestions for improvment or fittures to add are welcome)

## Starting Features
- Routes in seperate files in /routes directory
- Models in /models folder for auth
- Health endpoint at (`/health`)


## Installation

1. Clone the repository.
2. Run `make setup`.

```bash
make setup
```


## Running the Application

Run `make run` to start the server on `http://127.0.0.1:8000`.

The server will reload automatically on code changes.

```bash
make run
```

## .env file and variables

settings.py handles env variables look into it for more information 

## API Documentation

Once running, visit `http://127.0.0.1:8000/docs` for interactive API documentation provided by FastAPI.

## Dependencies

- FastAPI
- Uvicorn
- Pydantic

See `requirements.txt` for full list.

## Development

- `make clean` - Remove Python cache files
- `make freeze` - Update requirements.txt with current environment packages