"""
Area model
"""
from sqlalchemy import String, Row
from sqlalchemy.orm import Mapped, MappedColumn, relationship, Session
from .database import Base, engine


class Area(Base):  # pylint: disable=too-few-public-methods
    """
    Area model.
    """
    __tablename__ = "area"

    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str] = MappedColumn(String(255))

    apikeys: Mapped[list["Apikey"]] = relationship(  # type:ignore[name-defined]  # noqa: F821
        back_populates="area",
        cascade="all, delete-orphan",
    )


def get_area_by_name(area_name: str) -> Row[tuple[int]] | None:
    """
    Get area by name

    :param area_name: Area name
    :return: Area object or None
    """
    with Session(engine) as db:
        area = db.query(Area.id).filter(Area.name == area_name).first()
        db.close()

    return area
