"""
IZ-Analysis model
"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from barcodecheck_models.extensions import Base


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
