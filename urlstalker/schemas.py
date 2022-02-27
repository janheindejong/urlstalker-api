from datetime import datetime as DateTime, timezone

from pydantic import AnyHttpUrl, BaseModel, validator


class SnapShotBase(BaseModel):
    datetime: DateTime
    status_code: int
    response: str

    @validator("datetime")
    def dt_validate(cls, dt: DateTime):
        # This is necessary to ensure datetimes are always converted 
        # to UTC prior to storing in the DB (can only handle naive DT); 
        # and back to UTC for representation to the user
        return dt.astimezone(timezone.utc)


class SnapShot(SnapShotBase):
    id: int

    class Config:
        orm_mode = True


class ResourceBase(BaseModel):

    path: AnyHttpUrl


class Resource(ResourceBase):
    id: int
    snapshots: list[SnapShot] = []

    class Config:
        orm_mode = True
