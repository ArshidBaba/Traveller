# import asyncio
from typing import Any, Optional

# import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud


from app.api import deps

from app.schemas.package import (
    Package,
    PackageBase,
    PackageCreate,
    PackageSearchResults,
    PackageUpdate,
)

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


@router.get("/", status_code=200, response_model=PackageSearchResults)
def fetch_packages(
    *, max_results: Optional[int] = 10, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Get all Packages.
    """
    packages = crud.package.get_multi(db=db, limit=max_results)

    return {"results": packages}


# @router.get("/{location_id}", status_code=200, response_model=Location)
# def fetch_location(
#     *,
#     location_id: int,
#     db: Session = Depends(deps.get_db),
# ) -> Any:
#     """
#     Fetch a single recipe by ID
#     """
#     result = crud.location.get(db=db, id=location_id)
#     if not result:
#         # the exception is raised, not returned - you will get a validation
#         # error otherwise.
#         raise HTTPException(
#             status_code=404, detail=f"Recipe with ID {location_id} not found"
#         )


#     return result
@router.get("/{package_id}", status_code=200, response_model=Package)
def fetch_package(*, package_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    Fetch a single Package by ID.
    """
    result = crud.package.get(db=db, id=package_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Package with ID {package_id} not found"
        )
    return result
