from app import create_app, db
from seed import seed_categories, seed_terms


app = create_app()


with app.app_context():
    print("=" * 60)
    print("Tech Glossary Hub — Render Database Setup")
    print("=" * 60)

    print("Creating database tables...")
    db.create_all()

    print("Seeding categories...")
    seed_categories()

    print("Seeding glossary terms...")
    seed_terms()

    print("Database setup completed.")
    print("=" * 60)