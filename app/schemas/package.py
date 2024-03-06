from pydantic import BaseModel

from typing import Sequence


class PackageBase(BaseModel):
    name: str
    # description: str | None = None


class PackageCreate(PackageBase):
    name: str


class Package(PackageBase):
    # pass
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


class PackageUpdate(PackageBase):
    name: str


class PackageSearchResults(BaseModel):
    results: Sequence[Package]
