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

    def __repr__(self):
        return f"Level({self.id}, {self.name}, {self.description})"


class Languages(Base):
    __tablename__ = "Languages"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    courses = relationship("Courses", order_by="Courses.id", back_populates="language")

    def __repr__(self):
        return f"Language(id: {self.id}, name: {self.name})"


class Categories(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    courses = relationship("Courses", order_by="Courses.id", back_populates="category")

    def __repr__(self):
        return f"Category(id: {self.id}, name: {self.name})"


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

    def __repr__(self):
        return f"Course(" \
               f"id: {self.id}, " \
               f"lessons: {self.lessons}, " \
               f"description: {self.description}, " \
               f"start date: {self.start_date}, " \
               f"end date: {self.end_date}, " \
               f"price: {self.price}" \
               f")"


class LanguagesLimits(Base):
    __tablename__ = "LanguagesLimits"

    id = Column(Integer, primary_key=True)
    language_id = Column(Integer, ForeignKey(Languages.id))
    level_id = Column(Integer, ForeignKey(Levels.id))
