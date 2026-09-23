import subprocess
import sys

from app import create_app, db


app = create_app()


with app.app_context():
    print("=" * 60)
    print("Tech Glossary Hub — Render Database Setup")
    print("=" * 60)

    print("Creating database tables...")
    db.create_all()

print("Running database seed...")

subprocess.run(
    [sys.executable, "seed.py"],
    check=True
)

print("=" * 60)
print("Render database setup completed successfully.")
print("=" * 60)