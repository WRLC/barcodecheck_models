"""
RowTrayData model.
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class RowTrayData(Base):
    """
    RowTrayData model.
    """
    __tablename__ = 'rowtraydata'

    id: Mapped[int] = mapped_column(primary_key=True)
    barcode: Mapped[str] = mapped_column()  # Barcode
    internal_note_1: Mapped[str] = mapped_column(String(255))  # Internal note 1
    item_call_number: Mapped[str] = mapped_column(String(255))  # Item call number
    provenance_code: Mapped[str] = mapped_column(String(255))  # Provenance code

    def __repr__(self):
        return f"<RowTrayData(barcode={self.barcode}, provenance_code={self.provenance_code})>"

    def __str__(self):
        return f"{self.barcode} {self.provenance_code}"
