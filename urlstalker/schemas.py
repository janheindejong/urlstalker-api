from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel


class SnapShotBase(BaseModel):
    datetime: datetime
    status_code: int
    response: str


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
