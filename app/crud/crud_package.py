from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.package import Package
from app.schemas.package import PackageCreate, PackageUpdate


class CRUDPackage(CRUDBase[Package, PackageCreate, PackageUpdate]): ...


package = CRUDPackage(Package)
