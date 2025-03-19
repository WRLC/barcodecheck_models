"""
IZ model
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from .extensions import Base


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
