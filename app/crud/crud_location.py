from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.location import Location
from app.schemas.location import LocationCreate, LocationUpdate


class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]): ...


#     def update(
#         self,
#         db: Session,
#         *,
#         db_obj: Location,
#         obj_in: Union[LocationUpdate, Dict[str, Any]]
#     ) -> Location:
#         if isinstance(obj_in, dict):
#             update_data = obj_in
#         else:
#             update_data = obj_in.dict(exclude_unset=True)

#         return super().update(db, db_obj=db_obj, obj_in=update_data)


location = CRUDLocation(Location)
