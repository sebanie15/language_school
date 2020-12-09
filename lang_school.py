from abc import abstractmethod
from typing import List

from sqlalchemy import DateTime, Numeric
from db import Levels, Languages, Categories, Courses
from db.db_session import DBSession


class AbsLanguageSchool(DBSession):

    @abstractmethod
    def add_level(self, name: str, description: str) -> None:
        pass

    @abstractmethod
    def add_levels(self, levels: List[List[str]]) -> None:
        pass

    @abstractmethod
    def add_language(self, name: str) -> None:
        pass

    @abstractmethod
    def add_languages(self, languages: List[Languages]):
        pass

    @abstractmethod
    def add_category(self, name: str) -> None:
        pass

    @abstractmethod
    def add_course(self, no_lessons: int, description: str, language_id: int, category_id: int, level_id: int,
                   start_date: DateTime, end_date: DateTime, price: Numeric
                   ) -> None:
        pass


class LanguageSchool(AbsLanguageSchool):

    def add_level(self, level: str, description: str) -> None:
        self._session.add(
            Levels(
                name=level,
                description=description
            )
        )
        self._session.commit()

    def add_levels(self, levels: List[List[str]]) -> None:
        if levels:
            for level in levels:
                self._session.add(
                    Levels(
                        name=level[0],
                        description=level[1]
                    )
                )
            self._session.commit()

    def add_many_levels(self, levels: List[Levels]) -> None:
        if levels:
            self._session.add_all(levels)
            self._session.commit()

    def add_language(self, language_name: str) -> None:
        self._session.add(
            Languages(name=language_name)
        )
        self._session.commit()

    def add_languages(self, languages: List[str]):
        if languages:
            for language in languages:
                self._session.add(
                    Languages(
                        name=language
                    )
                )
            self._session.commit()

    def add_many_languages(self, languages: List[Languages]):
        if languages:
            self._session.add_all(languages)
            self._session.commit()

    def add_category(self, category_name: str) -> None:
        if category_name != '':
            self._session.add(
                Categories(name=category_name)
            )
            self._session.commit()

    def add_categories(self, categories: List[str]) -> None:
        if categories:
            for catgory in categories:
                self.session.add(
                    Categories(
                        name= catgory
                    )
                )

    def add_many_catgories(self, catogories: List[Categories]) -> None:
        if catogories:
            self._session.add_all(catogories)
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

    def levels(self, filter: str = '') -> List[Levels]:
        if filter != '':
            pass
        return self.session.query(Levels).all()


if __name__ == '__main__':

    db_connection = f"sqlite:///:memory:"
    school_1 = LanguageSchool(connection_string=db_connection)

    """"
    Language level and the number of hours of study
    C2 /ca 1000 – 1200 h
    C1 / ca 700 – 800 h
    B2 / ca 500 – 600 h
    B1 / ca 350 – 400 h
    A2 / ca 180 – 200 h
    A1 / ca 80 – 120 h
    """

    basescholl = DBSession(db_connection)
