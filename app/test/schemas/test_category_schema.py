import pytest
from app.schemas.category import Category

def test_category_schema():
    category = Category(
        name='Clothe',
        slug='clothe'
    )

    assert category.dict() == {
        'name': 'Clothe',
        'slug': 'clothe'
    }

def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name='Clothe',
            slug = 'bed clothe'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Clothe',
            slug='cão'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Clothe',
            slug='Clothe'
        )