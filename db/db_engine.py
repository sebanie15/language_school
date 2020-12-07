from abc import ABC

from sqlalchemy import create_engine

from db.db_structure import Base


class DBEngine(ABC):

    def __init__(self, connection_string: str, echo: bool = True) -> None:
        self.engine = create_engine(connection_string, echo=echo)
        Base.metadata.create_all(self.engine)
