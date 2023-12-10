from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from persistence.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    linked_in = Column(String, nullable=False)
    github = Column(String, nullable=False)
