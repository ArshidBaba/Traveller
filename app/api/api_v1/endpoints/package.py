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


# @router.get("/search/", status_code=200, response_model=LocationSearchResults)
# def search_locations(
#     *,
#     keyword: str = Query(None, min_length=3, example="Pahalgam"),
#     max_results: Optional[int] = 10,
#     db: Session = Depends(deps.get_db),
# ) -> dict:
#     """
#     Search for recipes based on label keyword
#     """
#     locations = crud.location.get_multi(db=db, limit=max_results)
#     results = filter(
#         lambda location: keyword.lower() in location.name.lower(), locations
#     )


#     return {"results": list(results)}
@router.get("/search/", status_code=200, response_model=PackageSearchResults)
def search_packages(
    *,
    keyword: str = Query(None, min_length=3, example="Deluxe"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for packages based on name keyword.
    """
    packages = crud.location.get_multi(db=db, limit=max_results)
    results = filter(lambda package: keyword.lower() in package.name.lower(), packages)
    return {"results": packages}
