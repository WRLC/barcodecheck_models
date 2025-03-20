"""
Database connection and base model for SQLAlchemy.
"""
import logging
import os
import sqlalchemy.exc
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

load_dotenv()  # Load environment variables from .env file

engine = create_engine(os.getenv("SQLALCHEMY_DB_URL"))  # type:ignore[arg-type] # Create a new SQLite database


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """
    Base class for all models.
    """
    pass  # pylint: disable=unnecessary-pass


def truncate_table(table_name: str) -> None | sqlalchemy.exc.SQLAlchemyError:
    """
    Truncate a table in the database.

    :param table_name: Name of the table to truncate
    """
    try:
        with Session(engine) as db:
            stmt = "TRUNCATE TABLE %s" % table_name
            db.execute(stmt)
            db.commit()
            db.close()
    except sqlalchemy.exc.SQLAlchemyError as e:
        logging.error(f"Error truncating table {table_name}: {e}")
        return e

    return None


def add_to_db(row: Base) -> None:
    """
    Add RowTrayData to the database.
    """
    with Session(engine) as db:
        db.add(row)
        db.commit()
        db.close()
