from abc import abstractmethod

from sqlalchemy import DateTime, Numeric
from db import Levels, Languages, Categories, Session, Courses, DBEngine


class BaseSchool(DBEngine):

    def __init__(self, connection_string: str, echo: bool = True):
        super().__init__(connection_string, echo)
        Session.configure(bind=self.engine)

        self._session = Session()

    @property
    def session(self) -> Session:
        return self._session


class AbsLanguageSchool(BaseSchool):

    @abstractmethod
    def add_level(self, name: str, description: str) -> None:
        pass

    @abstractmethod
    def add_language(self, name: str) -> None:
        pass

    @abstractmethod
    def add_categories(self, name: str) -> None:
        pass

    @abstractmethod
    def add_course(self, no_lessons: int, description: str, language_id: int, category_id: int, level_id: int,
                   start_date: DateTime, end_date: DateTime, price: Numeric
                   ) -> None:
        pass


class LanguageSchool(AbsLanguageSchool):

    def add_level(self, name: str, description: str) -> None:
        self._session.add(
            Levels(
                name=name,
                description=description
            )
        )
        self._session.commit()

    def add_language(self, name: str) -> None:
        self._session.add(
            Languages(name=name)
        )
        self._session.commit()

    def add_categories(self, name: str) -> None:
        self._session.add(
            Categories(name=name)
        )
        self._session.commit()

    def add_course(self, no_lessons: int, description: str, language_id: int, category_id: int, level_id: int,
                   start_date: DateTime, end_date: DateTime, price: Numeric
                   ) -> None:
        self._session.add(
            Courses(
                lessons=no_lessons,
                description=description,
                start_date=start_date,
                end_date=end_date,
                price=price,
                level_id=level_id,
                category_id=category_id,
                language_id=language_id
            )
        )
        pass


db_connection = f"sqlite:///:memory:"
school_1 = LanguageSchool(connection_string=db_connection)
school_1.add_level(name="A0", description="Podstawowy")
