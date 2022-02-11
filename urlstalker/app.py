"""FastAPI app"""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal

# FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/resource", response_model=list[schemas.Resource])
def get_resource(db: Session = Depends(get_db)) -> list[schemas.Resource]:
    resources = crud.get_resources(db)
    return resources


@app.post("/resource", response_model=schemas.Resource)
def get_resource(
    resource: schemas.ResourceBase, db: Session = Depends(get_db)
) -> schemas.Resource:
    return crud.create_new_resource(db, resource)


@app.post("/resource/{id}/snapshot", response_model=schemas.SnapShot)
def get_resource(
    id: int, snapshot: schemas.SnapShotBase, db: Session = Depends(get_db)
) -> schemas.SnapShot:
    return crud.add_snap_shot(db, id, snapshot)
