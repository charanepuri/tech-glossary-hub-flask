from app import create_app
from app.models import Category, GlossaryTerm


app = create_app()


with app.app_context():

    categories = Category.query.order_by(Category.name.asc()).all()
    terms = GlossaryTerm.query.order_by(GlossaryTerm.name.asc()).all()

    print()
    print("=" * 60)
    print("TECH GLOSSARY HUB — DATABASE CHECK")
    print("=" * 60)

    print(f"Total Categories : {len(categories)}")
    print(f"Total Terms      : {len(terms)}")

    print()
    print("CATEGORY COUNTS")
    print("-" * 60)

    for category in categories:
        count = GlossaryTerm.query.filter_by(
            category_id=category.id
        ).count()

        print(
            f"{category.name:<32} {count:>3}"
        )

    print()
    print("LEVEL COUNTS")
    print("-" * 60)

    for level in ["Beginner", "Moderate", "Advanced"]:

        count = GlossaryTerm.query.filter_by(
            level=level
        ).count()

        print(
            f"{level:<15} {count:>3}"
        )

    print()
    print("=" * 60)