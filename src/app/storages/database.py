import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://shedko:postgres@localhost:5432/vek_news')


Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    """get session"""
    session = Session()
    logging.info(f'Новая сессия подключения к БД создана.')
    try:
        yield session
    finally:
        logging.info(f'Сессия подключения к БД закрыта.')
        session.close()
