# URL Stalker

Pet project to stalk HTTP endpoints - taking snapshots at regular intervals. 

## User stories 

In order of implementation importance:

1. As a Jan Hein, I want to be able to add a URL for tracking with that gets

## Architecture 

We'll use the following techniques: 

- FastAPI and OpenAPI for creating the API for the user to register and manage the URLs
- SQLlite database for storing URLs, stored 
- SQLAlchemy for ORM / manual
- Separate application for executing the requests / separate thread?

