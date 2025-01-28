from app.use_cases.category import CategoryUseCase
from app.db.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput

def test_add_category_uc(db_session):
    uc = CategoryUseCase(db_session)

    category = Category(
        name= 'Clothe',
        slug= 'clothe'
    )

    uc.add_category(category=category)

    categories_db_list = db_session.query(CategoryModel).all()
    assert len(categories_db_list) == 1
    assert categories_db_list[0].name == 'Clothe'
    assert categories_db_list[0].slug == 'clothe'

    db_session.delete(categories_db_list[0])
    db_session.commit()

def test_list_categories(db_session, categories_on_db):
    uc = CategoryUseCase(db_session=db_session)

    categories = uc.list_categories()

    assert  len(categories) == 4
    assert  type(categories[0]) == CategoryOutput
    assert categories[0].id == categories_on_db[0].id
    assert categories[0].name == categories_on_db[0].name
    assert categories[0].slug == categories_on_db[0].slug
