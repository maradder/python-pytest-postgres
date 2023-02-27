import os
import sys

import pytest
from dotenv import load_dotenv

sys.path.append(os.getcwd())
from main import get_items
from database import Database


# Create a pytest fixture to create a database session for testing
@pytest.fixture
def session():
    # Clear the environment variables and load the test environment variables
    os.environ.clear()
    load_dotenv(".test.env")

    # Create a db config object to pass to the Database class
    db_config = {
        "drivername": "postgresql",
        "username": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "database": os.getenv("DB_NAME"),
    }

    # Pass the db config object to the Database class, create a session, and get the session
    db = Database(db_config)
    db.create_session()
    test_session = db.get_session()

    # Pass the session to the test function
    yield test_session

    # Close the session after the test function has finished
    return db.close_session()


# Test the get_items function with the test session
def test_get_items_length(session):
    items = get_items(session)
    assert len(items) == 2

def test_get_items_item_name(session):
    items = get_items(session)
    assert items[1].item_name == "test item 2"

