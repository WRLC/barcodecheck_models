"""
Area model
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from barcodecheck_models.extensions import Base


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
