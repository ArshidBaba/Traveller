from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Package(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    # description = Column(String(256), index=True, nullable=True)
