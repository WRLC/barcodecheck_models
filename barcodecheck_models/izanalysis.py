"""
IZ-Analysis model
"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from .analysis import Analysis
from .iz import IZ
from .database import Base, engine


class IZAnalysis(Base):  # pylint: disable=too-few-public-methods
    """
    IZ-Analysis model.
    """
    __tablename__ = "iz_analysis"

    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[str] = mapped_column(String(255))  # Path
    iz_id: Mapped[int] = mapped_column(ForeignKey('iz.id'))  # IZ code
    analysis_id: Mapped[int] = mapped_column(ForeignKey('analysis.id'))  # Analysis ID

    iz: Mapped["IZ"] = relationship(back_populates="izanalyses")  # type:ignore[name-defined]  # noqa: F821
    analysis: Mapped["Analysis"] = relationship(back_populates="izanalyses")  # type:ignore[name-defined]  # noqa: F821


def get_iz_analysis_by_iz_and_analysis(iz: IZ, analysis: Analysis) -> IZAnalysis | None:
    """
    Get report path by IZ and analysis

    :param iz: IZ object
    :param analysis: Analysis object
    :return: Report path or None
    """
    with Session(engine) as db:
        iz_analysis = db.query(IZAnalysis).filter(IZAnalysis.iz_id == iz.id, IZAnalysis.analysis_id == analysis.id).first()
        db.close()

    return iz_analysis
