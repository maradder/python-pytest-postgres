from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


# Create a base class for the models
Base = declarative_base()

# Create a model for the items in the items table
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)