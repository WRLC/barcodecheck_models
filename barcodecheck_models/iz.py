"""
IZ model
"""
from sqlalchemy import String, Row
from sqlalchemy.orm import Mapped, MappedColumn, relationship, Session
from .database import Base, engine


class IZ(Base):  # pylint: disable=too-few-public-methods
    """
    IZ model.
    """
    __tablename__ = "iz"

    id: Mapped[int] = MappedColumn(primary_key=True)  # IZ ID
    code: Mapped[str] = MappedColumn(String(255))  # IZ code
    name: Mapped[str] = MappedColumn(String(255))  # IZ name

    apikeys: Mapped[list["Apikey"]] = relationship(  # type:ignore[name-defined]  # noqa: F821
        back_populates="iz",
        cascade="all, delete-orphan",
    )

    izanalyses: Mapped[list["IZAnalysis"]] = relationship(  # type:ignore[name-defined]  # noqa: F821
        back_populates="iz",
        cascade="all, delete-orphan",
    )


def get_iz_by_code(iz_code: str) -> Row[tuple[int]] | None:
    """
    Get IZ by code

    :param iz_code: IZ code
    :return: IZ object or None
    """
    with Session(engine) as db:
        iz = db.query(IZ.id).filter(IZ.code == iz_code).first()
        db.close()

    return iz
