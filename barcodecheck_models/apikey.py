"""
API Key Model
"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from .database import Base, engine


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


def get_api_key_by_area_and_iz(area_id: int, iz_id: int, write_code: bool) -> Apikey | None:
    """
    Get API key by area and IZ

    :param area_id: Area ID
    :param iz_id: IZ ID
    :param write_code: Write access
    :return: API key or None
    """
    with Session(engine) as db:
        apikey = db.query(Apikey).filter(
            Apikey.area_id == area_id, Apikey.iz_id == iz_id, Apikey.writekey == write_code
        ).first()
        db.close()

    return apikey
