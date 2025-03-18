"""
API Key Model
"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from barcodecheck_models.extensions import Base


class Apikey(Base):  # pylint: disable=too-few-public-methods
    """
    API Key model.
    """
    __tablename__ = "api_key"

    id: Mapped[int] = mapped_column(primary_key=True)  # Key ID
    apikey: Mapped[str] = mapped_column(String(255))  # Key value
    writekey: Mapped[bool] = mapped_column()  # Write access
    area_id: Mapped[int] = mapped_column(ForeignKey("area.id"))  # Area ID
    iz_id: Mapped[int] = mapped_column(ForeignKey("iz.id"))  # IZ ID

    area: Mapped["Area"] = relationship(back_populates="apikeys")  # type:ignore[name-defined]  # noqa: F821
    iz: Mapped["IZ"] = relationship(back_populates="apikeys")  # type:ignore[name-defined]  # noqa: F821
