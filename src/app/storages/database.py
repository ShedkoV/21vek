from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:postgres@localhost/vek_news")


Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    """get session"""
    session = Session()
    try:
        yield session
    finally:
        session.close()
