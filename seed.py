from app import create_app, db
from app.models import Category, GlossaryTerm


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

terms = [
    {
        "name": "Flask",
        "slug": "flask",
        "definition": (
            "Flask is a lightweight Python web framework used to build "
            "web applications and APIs. It provides routing, request "
            "handling, templating, and other essential web development "
            "capabilities."
        ),
        "example": (
            "from flask import Flask\n\n"
            "app = Flask(__name__)\n\n"
            "@app.route('/')\n"
            "def home():\n"
            "    return 'Hello, Flask!'"
        ),
        "category_slug": "flask-microframeworks",
    },
    {
        "name": "Jinja2",
        "slug": "jinja2",
        "definition": (
            "Jinja2 is a Python template engine used by Flask to generate "
            "dynamic HTML pages. It allows Python-style expressions, "
            "variables, conditions, loops, and template inheritance."
        ),
        "example": (
            "<h1>{{ title }}</h1>\n\n"
            "{% for item in items %}\n"
            "    <p>{{ item }}</p>\n"
            "{% endfor %}"
        ),
        "category_slug": "flask-microframeworks",
    },
    {
        "name": "REST",
        "slug": "rest",
        "definition": (
            "REST, or Representational State Transfer, is an architectural "
            "style for designing networked applications. REST APIs commonly "
            "use HTTP methods to perform operations on resources."
        ),
        "example": (
            "GET /api/users\n"
            "POST /api/users\n"
            "PUT /api/users/1\n"
            "DELETE /api/users/1"
        ),
        "category_slug": "rest-apis",
    },
    {
        "name": "CRUD",
        "slug": "crud",
        "definition": (
            "CRUD represents the four basic operations performed on data: "
            "Create, Read, Update, and Delete."
        ),
        "example": (
            "Create  → POST\n"
            "Read    → GET\n"
            "Update  → PUT / PATCH\n"
            "Delete  → DELETE"
        ),
        "category_slug": "rest-apis",
    },
    {
        "name": "Blueprint",
        "slug": "blueprint",
        "definition": (
            "A Flask Blueprint is a way to organize related routes, "
            "views, and other application components into reusable modules."
        ),
        "example": (
            "main_bp = Blueprint('main', __name__)\n\n"
            "@main_bp.route('/')\n"
            "def home():\n"
            "    return 'Home'"
        ),
        "category_slug": "backend-architecture",
    },
    {
        "name": "Application Factory",
        "slug": "application-factory",
        "definition": (
            "The application factory pattern creates a Flask application "
            "inside a function. It improves application organization, "
            "configuration, testing, and support for multiple instances."
        ),
        "example": (
            "def create_app():\n"
            "    app = Flask(__name__)\n"
            "    return app"
        ),
        "category_slug": "backend-architecture",
    },
    {
        "name": "Session",
        "slug": "session",
        "definition": (
            "A session allows a web application to store information "
            "associated with a user's interaction across multiple requests."
        ),
        "example": (
            "session['username'] = 'developer'"
        ),
        "category_slug": "web-authentication",
    },
    {
        "name": "JWT",
        "slug": "jwt",
        "definition": (
            "JSON Web Token is a compact token format commonly used to "
            "represent claims between parties and support stateless "
            "authentication in web applications and APIs."
        ),
        "example": (
            "Authorization: Bearer <token>"
        ),
        "category_slug": "web-authentication",
    },
    {
        "name": "ORM",
        "slug": "orm",
        "definition": (
            "Object-Relational Mapping is a technique that allows "
            "developers to interact with relational database data "
            "using programming language objects."
        ),
        "example": (
            "user = User.query.filter_by(username='charan').first()"
        ),
        "category_slug": "databases-orm",
    },
    {
        "name": "SQLAlchemy",
        "slug": "sqlalchemy",
        "definition": (
            "SQLAlchemy is a Python SQL toolkit and Object-Relational "
            "Mapper that provides tools for working with relational "
            "databases."
        ),
        "example": (
            "class User(db.Model):\n"
            "    id = db.Column(db.Integer, primary_key=True)"
        ),
        "category_slug": "databases-orm",
    },
    {
        "name": "CORS",
        "slug": "cors",
        "definition": (
            "Cross-Origin Resource Sharing is a browser security mechanism "
            "that controls whether requests from one origin can access "
            "resources from another origin."
        ),
        "example": (
            "Access-Control-Allow-Origin: https://example.com"
        ),
        "category_slug": "web-security",
    },
    {
        "name": "XSS",
        "slug": "xss",
        "definition": (
            "Cross-Site Scripting is a web security vulnerability where "
            "malicious scripts can be injected into content delivered to "
            "other users."
        ),
        "example": (
            "Always validate and safely escape untrusted user input "
            "before rendering it."
        ),
        "category_slug": "web-security",
    },
    {
        "name": "Caching",
        "slug": "caching",
        "definition": (
            "Caching stores frequently accessed data temporarily so that "
            "future requests can be served faster and with less processing."
        ),
        "example": (
            "Frequently requested API results can be stored temporarily "
            "instead of querying the database for every request."
        ),
        "category_slug": "web-performance",
    },
    {
        "name": "Unit Testing",
        "slug": "unit-testing",
        "definition": (
            "Unit testing verifies individual units of application code "
            "in isolation to ensure they behave as expected."
        ),
        "example": (
            "def test_home(client):\n"
            "    response = client.get('/')\n"
            "    assert response.status_code == 200"
        ),
        "category_slug": "testing-debugging",
    },
    {
        "name": "Celery",
        "slug": "celery",
        "definition": (
            "Celery is a distributed task queue system commonly used "
            "with Python applications to execute background tasks."
        ),
        "example": (
            "A Flask application can delegate a long-running task "
            "to a Celery worker instead of blocking the web request."
        ),
        "category_slug": "background-processing",
    },
    {
        "name": "Gunicorn",
        "slug": "gunicorn",
        "definition": (
            "Gunicorn is a Python WSGI HTTP server commonly used to "
            "serve Python web applications in production."
        ),
        "example": (
            "gunicorn run:app"
        ),
        "category_slug": "web-deployment",
    },
    {
        "name": "MVC",
        "slug": "mvc",
        "definition": (
            "Model-View-Controller is an architectural pattern that "
            "separates application data, presentation, and request "
            "handling responsibilities."
        ),
        "example": (
            "Model → Data\n"
            "View → Presentation\n"
            "Controller → Request and application logic"
        ),
        "category_slug": "software-architecture",
    },
    {
        "name": "Virtual Environment",
        "slug": "virtual-environment",
        "definition": (
            "A Python virtual environment creates an isolated environment "
            "where a project can install and manage its own dependencies."
        ),
        "example": (
            "python -m venv venv\n"
            ".\\venv\\Scripts\\Activate.ps1"
        ),
        "category_slug": "python-web-ecosystem",
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


        for term_data in terms:

            existing_term = GlossaryTerm.query.filter_by(
                slug=term_data["slug"]
            ).first()

            if existing_term:
                continue


            category = Category.query.filter_by(
                slug=term_data["category_slug"]
            ).first()


            if not category:
                print(
                    f"Category not found for {term_data['name']}"
                )

                continue


            glossary_term = GlossaryTerm(
                name=term_data["name"],
                slug=term_data["slug"],
                definition=term_data["definition"],
                example=term_data["example"],
                category_id=category.id
            )


            db.session.add(glossary_term)


        db.session.commit()


        print("Categories and glossary terms seeded successfully.")
        
if __name__ == "__main__":
    seed_categories()