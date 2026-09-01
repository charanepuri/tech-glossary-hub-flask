from app import create_app
from app.models import Category, GlossaryTerm


app = create_app()


with app.app_context():

    categories = Category.query.order_by(
        Category.name.asc()
    ).all()

    terms = GlossaryTerm.query.order_by(
        GlossaryTerm.name.asc()
    ).all()


    print(
        f"\nTotal categories: {len(categories)}"
    )

    print(
        f"Total glossary terms: {len(terms)}\n"
    )


    print("CATEGORIES")
    print("=" * 40)

    for category in categories:
        print(
            f"{category.id}. "
            f"{category.name} "
            f"({len(category.terms)} terms)"
        )


    print("\nGLOSSARY TERMS")
    print("=" * 40)

    for term in terms:
        print(
            f"{term.id}. "
            f"{term.name} → "
            f"{term.category.name}"
        )