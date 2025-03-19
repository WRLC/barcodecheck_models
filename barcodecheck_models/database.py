"""
Database connection and base model for SQLAlchemy.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(os.getenv("SQLALCHEMY_DB_URL"))  # type:ignore[arg-type] # Create a new SQLite database


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """
    Base class for all models.
    """
    pass  # pylint: disable=unnecessary-pass
