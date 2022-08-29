import os
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv(".env")

engine = create_engine(os.getenv('DATABASE_URL'), pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class Base:
    id: Any
    __name__: str
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()