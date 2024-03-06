import asyncio
from typing import Any, Optional

# import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud

# from app.crud.crud_location import CRUDLocation
from app.api import deps

from app.schemas.recipe import Recipe, RecipeCreate, RecipeSearchResults
from app.schemas.location import (
    Location,
    LocationBase,
    LocationCreate,
    LocationSearchResults,
    LocationUpdate,
)

router = APIRouter()
# RECIPE_SUBREDDITS = ["recipes", "easyrecipes", "TopSecretRecipes"]


@router.get("/{location_id}", status_code=200, response_model=Location)
def fetch_location(
    *,
    location_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = crud.location.get(db=db, id=location_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {location_id} not found"
        )

    return result


@router.get("/search/", status_code=200, response_model=LocationSearchResults)
def search_locations(
    *,
    keyword: str = Query(None, min_length=3, example="Pahalgam"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for recipes based on label keyword
    """
    locations = crud.location.get_multi(db=db, limit=max_results)
    results = filter(
        lambda location: keyword.lower() in location.name.lower(), locations
    )

    return {"results": list(results)}


@router.post("/", status_code=201, response_model=Location)
def create_location(
    *, location_in: LocationCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new recipe in the database.
    """
    location = crud.location.create(db=db, obj_in=location_in)

    return location


@router.put("/{location_id}", status_code=200, response_model=LocationUpdate)
def update_location(
    *, location_id: int, location_in: LocationUpdate, db: Session = Depends(deps.get_db)
) -> Any:
    """
    Updates a single Location.
    """

    db_obj = crud.location.get(db=db, id=location_id)
    location = crud.location.update(db_obj=db_obj, obj_in=location_in, db=db)

    return location


# async def get_reddit_top_async(subreddit: str) -> list:
#     async with httpx.AsyncClient() as client:
#         response = await client.get(
#             f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
#             headers={"User-agent": "recipe bot 0.1"},
#         )

#     subreddit_recipes = response.json()
#     subreddit_data = []
#     for entry in subreddit_recipes["data"]["children"]:
#         score = entry["data"]["score"]
#         title = entry["data"]["title"]
#         link = entry["data"]["url"]
#         subreddit_data.append(f"{str(score)}: {title} ({link})")
#     return subreddit_data


# def get_reddit_top(subreddit: str) -> list:
#     response = httpx.get(
#         f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
#         headers={"User-agent": "recipe bot 0.1"},
#     )
#     subreddit_recipes = response.json()
#     subreddit_data = []
#     for entry in subreddit_recipes["data"]["children"]:
#         score = entry["data"]["score"]
#         title = entry["data"]["title"]
#         link = entry["data"]["url"]
#         subreddit_data.append(f"{str(score)}: {title} ({link})")
#     return subreddit_data


# @router.get("/ideas/async")
# async def fetch_ideas_async() -> dict:
#     results = await asyncio.gather(
#         *[get_reddit_top_async(subreddit=subreddit) for subreddit in RECIPE_SUBREDDITS]
#     )
#     return dict(zip(RECIPE_SUBREDDITS, results))


# @router.get("/ideas/")
# def fetch_ideas() -> dict:
#     return {key: get_reddit_top(subreddit=key) for key in RECIPE_SUBREDDITS}
