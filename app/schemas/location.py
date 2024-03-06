from pydantic import BaseModel

from typing import Sequence


class LocationBase(BaseModel):
    name: str
    description: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    name: str
    description: str


class LocationUpdate(LocationBase):
    name: str
    description: str


# # Properties shared by models stored in DB
class LocationInDBBase(LocationBase):
    id: int

    class Config:
        orm_mode = True


# # Properties to return to client
class Location(LocationInDBBase):
    # pass
    # id: int
    name: str
    description: str


# # Properties properties stored in DB
class LocationInDB(LocationInDBBase):
    pass


class LocationSearchResults(BaseModel):
    results: Sequence[Location]
