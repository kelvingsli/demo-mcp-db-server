from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    code_name = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.full_name}, code_name={self.code_name})>"