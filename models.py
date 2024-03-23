from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Family(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True)
    users = relationship('User', backref='family') # family:1, user:many
    time_capsules = relationship('TimeCapsule', backref='family') # family:1, time_capsule:many

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    family_id = Column(Integer, ForeignKey('families.id')) # user:1, family:many
    name = Column(String)
    password = Column(String) # TODO: 余裕があったらハッシュして
    age = Column(Integer)
    type = Column(Enum('parent', 'child'))

class TimeCapsule(Base):
    __tablename__ = 'time_capsules'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) # time_capsule:1, user:many
    family_id = Column(Integer, ForeignKey('families.id')) # time_capsule:mamy, family:1
    title = Column(String)
    content = Column(String)
    creted_at = Column(Date)
    updated_at = Column(Date)
    images = relationship('Image', backref='time_capsule') # time_capsule:1, image:many

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    time_capsule_id = Column(Integer, ForeignKey('time_capsules.id')) # image:1, time_capsule:many
    path = Column(String) # NOTE：(images/) + pathで画像にアクセスできるイメージ
    created_at = Column(Date)
    updated_at = Column(Date)