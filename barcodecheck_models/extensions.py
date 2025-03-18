import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

dotenv.load_dotenv()

engine = create_engine(os.getenv("SQLALCHEMY_DB_URL"))  # type:ignore[arg-type] # Create a new SQLite database


class Base(DeclarativeBase):
    """
    Base class for all models.
    """
    pass  # pylint: disable=unnecessary-pass
