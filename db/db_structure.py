from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Levels(Base):
    __tablename__ = "Levels"

    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    description = Column(String(40))

    courses = relationship("Courses", order_by="Courses.id", back_populates="level")


class Languages(Base):
    __tablename__ = "Languages"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    courses = relationship("Courses", order_by="Courses.id", back_populates="language")


class Categories(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    courses = relationship("Courses", order_by="Courses.id", back_populates="category")


class Courses(Base):
    __tablename__ = "Courses"

    id = Column(Integer, primary_key=True)
    lessons = Column(Integer)
    description = Column(String(30))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    price = Column(Numeric)
    level_id = Column(Integer, ForeignKey(Levels.id))
    category_id = Column(Integer, ForeignKey(Categories.id))
    language_id = Column(Integer, ForeignKey(Languages.id))

    level = relationship(Levels, back_populates="courses")
    language = relationship(Languages, back_populates="courses")
    category = relationship(Categories, back_populates="courses")
