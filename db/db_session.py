from sqlalchemy.orm import sessionmaker

from db.db_engine import DBEngine

Session = sessionmaker()


class DBSession(DBEngine):

    def __init__(self, connection_string: str, echo: bool = True):
        super().__init__(connection_string, echo)
        Session.configure(bind=self.engine)

        self._session = Session()

    @property
    def session(self) -> Session:
        return self._session

    @session.setter
    def session(self, session: Session):
        if session:
            self._session = session
