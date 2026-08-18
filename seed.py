from app import create_app, db
from app.models import Category


categories = [
    {
        "name": "Flask & Microframeworks",
        "slug": "flask-microframeworks",
        "description": (
            "Concepts related to Flask and Python microframeworks."
        ),
    },
    {
        "name": "REST APIs",
        "slug": "rest-apis",
        "description": (
            "REST architecture, HTTP methods, APIs, JSON, and CRUD concepts."
        ),
    },
    {
        "name": "Backend Architecture",
        "slug": "backend-architecture",
        "description": (
            "Core concepts used to design and structure backend applications."
        ),
    },
    {
        "name": "Web Authentication",
        "slug": "web-authentication",
        "description": (
            "Authentication, authorization, sessions, cookies, JWT, and OAuth."
        ),
    },
    {
        "name": "Databases & ORM",
        "slug": "databases-orm",
        "description": (
            "Database concepts, ORM, SQLAlchemy, relationships, and transactions."
        ),
    },
    {
        "name": "Web Security",
        "slug": "web-security",
        "description": (
            "Important security concepts for modern web applications."
        ),
    },
    {
        "name": "Web Performance",
        "slug": "web-performance",
        "description": (
            "Caching, optimization, compression, rate limiting, and scalability."
        ),
    },
    {
        "name": "Testing & Debugging",
        "slug": "testing-debugging",
        "description": (
            "Testing, debugging, pytest, mocking, and application quality."
        ),
    },
    {
        "name": "Background Processing",
        "slug": "background-processing",
        "description": (
            "Task queues, workers, Redis, Celery, and asynchronous processing."
        ),
    },
    {
        "name": "Web Deployment",
        "slug": "web-deployment",
        "description": (
            "Production deployment, Gunicorn, Nginx, configuration, and hosting."
        ),
    },
    {
        "name": "Software Architecture",
        "slug": "software-architecture",
        "description": (
            "Architecture patterns and principles for maintainable applications."
        ),
    },
    {
        "name": "Python Web Ecosystem",
        "slug": "python-web-ecosystem",
        "description": (
            "Python environments, packages, extensions, and web development tools."
        ),
    },
]


def seed_categories():
    app = create_app()

    with app.app_context():
        for category_data in categories:
            existing_category = Category.query.filter_by(
                slug=category_data["slug"]
            ).first()

            if existing_category:
                continue

            category = Category(**category_data)

            db.session.add(category)

        db.session.commit()

        print("Categories seeded successfully.")


if __name__ == "__main__":
    seed_categories()