import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

dotenv.load_dotenv()

engine = create_engine(os.getenv("SQLALCHEMY_DB_URL"))  # type:ignore[arg-type] # Create a new SQLite database
session_factory = sessionmaker(bind=engine)  # Create a session factory


class Base(DeclarativeBase):
    """
    Base class for all models.
    """
    pass  # pylint: disable=unnecessary-pass
