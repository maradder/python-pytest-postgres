import os

from dotenv import load_dotenv

from models import Item
from database import Database

# Load the environment variables from the .env file unless another filepath is specified
load_dotenv()

# Create a db config object to pass to the Database class
# the environment variables for this object are set in the .env file
# loaded by the load_dotenv() function above
db_config = {
    "drivername": "postgresql",
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME")
}


# Pass the db config object to the Database class, create a session, and get the session
db = Database(db_config)
db.create_session()
session = db.get_session()


# Sample function to get all items from the database
def get_items(session):
    items = session.query(Item).all()
    return items


if __name__ == "__main__":
    items = get_items(session)
    print(items)


