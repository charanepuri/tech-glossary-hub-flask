from app import create_app
from app.models import Category


app = create_app()


with app.app_context():
    categories = Category.query.order_by(Category.name).all()

    print(f"\nTotal categories: {len(categories)}\n")

    for category in categories:
        print(
            f"{category.id}. "
            f"{category.name} "
            f"({category.slug})"
        )