from sqlalchemy import UUID, Column, Integer, String
from database import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True))
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
