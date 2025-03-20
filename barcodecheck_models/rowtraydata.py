"""
RowTrayData model.
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base, add_to_db, truncate_table


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


def handle_rowtraydata(
        rows: list[dict[str, str]],
        columns: dict[str, str]
) -> dict[str, int] | sqlalchemy.exc.SQLAlchemyError:
    """
    Handle the row data for the tray data

    :param rows: Row data
    :param columns: Columns dictionary
    :return: None
    """
    success = 0  # Initialize success counter
    error = 0  # Initialize error counter

    # truncate the table
    truncate = truncate_table(RowTrayData.__tablename__)

    if truncate:  # If truncate is not successful
        return truncate  # Return the error

    for row in rows:  # Iterate through the rows
        # Get the values from the row
        barcode: str = row[columns['Barcode']] if row[columns['Barcode']] else ''
        internal_note_1: str = row[columns['Internal Note 1']] if row[columns['Internal Note 1']] else ''
        item_call_number: str = row[columns['Item Call Number']] if row[columns['Item Call Number']] else ''
        provenance_code: str = row[columns['Provenance Code']] if row[columns['Provenance Code']] else ''

        rowtraydata = RowTrayData(
            barcode=barcode,
            internal_note_1=internal_note_1,
            item_call_number=item_call_number,
            provenance_code=provenance_code
        )

        try:
            add_to_db(rowtraydata)  # Add the row to the database
        except sqlalchemy.exc.SQLAlchemyError as e:
            logging.error("Error adding row to database: %s", e)  # Log the error
            error += 1
            continue

        success += 1  # Increment success counter

    return {'success': success, 'errors': error}  # Return None if successful
