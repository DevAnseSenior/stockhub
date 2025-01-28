import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModels

@pytest.fixture()
def db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture()
def categories_on_db(db_session):
    categories =  [
        CategoryModels(name='Clothe', slug='clothe'),
        CategoryModels(name='Car', slug='car'),
        CategoryModels(name='Kitchen', slug='kitchen'),
        CategoryModels(name='Decoration', slug='decoration'),
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()