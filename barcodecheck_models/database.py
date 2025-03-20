"""
Database connection and base model for SQLAlchemy.
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()  # Load environment variables from .env file

engine = create_engine(os.getenv("SQLALCHEMY_DB_URL"))  # type:ignore[arg-type] # Create a new SQLite database


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """
    Base class for all models.
    """
    pass  # pylint: disable=unnecessary-pass


def add_to_db(row: Base) -> None:
    """
    Add RowTrayData to the database.
    """
    with Session(engine) as db:
        db.add(row)
        db.commit()
        db.close()
