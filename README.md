# URL Stalker

Pet project to stalk HTTP endpoints - taking snapshots at regular intervals. The idea is that you can add a URL, and that the app will check and store the content of the URL on a daily basis. Additional features could storing only a part of it using RegEx; getting e-mails whenever something changes; doing some data analysis on the data. 

Don't know if it's really useful, but kinda fun. 

## Architecture 

We'll use the following techniques: 

- FastAPI and OpenAPI for creating the API for the user to register and manage the URLs
- SQLlite database for storing URLs, stored 
- SQLAlchemy for ORM
- Separate application for executing the requests


# Notes 

For typehinting with SQLAlchemy to work properly, you need to add the stubs like so: `poetry add sqlalchemy[mypy]`
