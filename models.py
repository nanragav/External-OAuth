from sqlalchemy import UUID, Column, String, BigInteger, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4

class User(Base):

    __tablename__ = 'users'

    id = Column(String(36), default=uuid4, nullable=False)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    session = Column(String(36), nullable=False, default=uuid4)

    drives = relationship('Drive', back_populates='owner')

    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_users_id'),
    )

class Drive(Base):

    __tablename__ = 'drive'

    id = Column(String(36), nullable = False, default= uuid4)
    file_name = Column(String(255), nullable=False)
    file_id = Column(BigInteger, nullable=False)
    user_id = Column(String(36), nullable=False)

    owner = relationship('User', back_populates='drives')

    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_drive_id'),
        ForeignKeyConstraint(['user_id'], refcolumns=['users.id'],  name='fk_drive_users_id')
    )