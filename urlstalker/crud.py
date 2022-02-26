from typing import Optional

from sqlalchemy.orm import Session, selectinload

from . import models, schemas


class ResourceNotFound(Exception):
    ...


def get_resources(db: Session) -> list[models.Resource]:
    return (
        db.query(models.Resource).options(selectinload(models.Resource.snapshots)).all()
    )


def create_new_resource(db: Session, obj_in: schemas.ResourceBase) -> models.Resource:
    resource = models.Resource(**obj_in.dict())
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return resource


def add_snap_shot(
    db: Session, id: int, obj_in: schemas.SnapShotBase
) -> models.SnapShot:
    resource: Optional[models.Resource] = db.query(models.Resource).get(id)
    if not resource:
        raise ResourceNotFound
    snapshot = models.SnapShot(resource_id=id, **obj_in.dict())
    resource.snapshots.append(snapshot)
    db.commit()
    db.refresh(snapshot)
    return snapshot
