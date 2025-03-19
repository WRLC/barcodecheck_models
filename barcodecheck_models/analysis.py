"""
Analysis models
"""
from sqlalchemy import String, Row
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from .database import Base, engine


class Analysis(Base):  # pylint: disable=too-few-public-methods
    """
    Analysis model.
    """
    __tablename__ = "analysis"

    id: Mapped[int] = mapped_column(primary_key=True)  # Analysis ID
    name: Mapped[str] = mapped_column(String(255))  # Analysis name

    izanalyses: Mapped[list["IZAnalysis"]] = relationship(  # type:ignore[name-defined]  # noqa: F821
        back_populates="analysis",
        cascade="all, delete-orphan",
    )


def get_analysis_by_name(analysis_name: str) -> Analysis | None:
    """
    Get analysis by name

    :param analysis_name: Analysis name
    :return: Analysis object or None
    """
    with Session(engine) as db:
        analysis = db.query(Analysis).filter(Analysis.name == analysis_name).first()
        db.close()

    return analysis
