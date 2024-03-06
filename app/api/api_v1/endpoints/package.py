# import asyncio
from typing import Any, Optional

# import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud


from app.api import deps

from app.schemas.package import Package, PackageBase, PackageCreate, PackageUpdate

router = APIRouter()


@router.post("/", status_code=201, response_model=Package)
def create_package(
    *, package_in: PackageCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new package in the database.
    """
    package = crud.package.create(db=db, obj_in=package_in)

    return package


# @router.put("/{location_id}", status_code=200, response_model=LocationUpdate)
# def update_location(
#     *, location_id: int, location_in: LocationUpdate, db: Session = Depends(deps.get_db)
# ) -> Any:
#     """
#     Updates a single Location.
#     """

#     db_obj = crud.location.get(db=db, id=location_id)
#     location = crud.location.update(db_obj=db_obj, obj_in=location_in, db=db)


#     return location
@router.put("/{package_id}", status_code=200, response_model=Package)
def update_package(
    *, package_id: int, package_in: PackageUpdate, db: Session = Depends(deps.get_db)
) -> Any:
    """
    Updates a single Package.
    """

    db_obj = crud.package.get(db=db, id=package_id)
    package = crud.package.update(db_obj=db_obj, obj_in=package_in, db=db)

    return package
