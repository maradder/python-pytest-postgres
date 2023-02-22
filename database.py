from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session


# Create a class to handle the database connection.
class Database:
    '''
    This class handles the database connection.

    Attributes:
        config (dict): A dictionary containing the database configuration.
        session (Session): A SQLAlchemy session object.
        url_object (URL): A SQLAlchemy URL object.

    Methods:
        create_session: Creates a SQLAlchemy session object.
        get_session: Returns the SQLAlchemy session object.
    '''
    def __init__(self, config):
        self.config = config
        self.session = None
        self.url_object = URL.create(
            drivername=self.config["drivername"],
            username=self.config["username"],
            password=self.config["password"],
            host=self.config["host"],
            port=self.config["port"],   
            database=self.config["database"]
        )

    def create_session(self):
        engine = create_engine(self.url_object)
        self.session = Session(engine)

    def get_session(self):
        return self.session