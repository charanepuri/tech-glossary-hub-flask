from app import create_app, db
from app.models import Category, GlossaryTerm


# ============================================================
# CATEGORIES
# ============================================================

categories = [
    {
        "name": "Flask & Microframeworks",
        "slug": "flask-microframeworks",
        "description": "Concepts related to Flask and Python microframeworks.",
    },
    {
        "name": "REST APIs",
        "slug": "rest-apis",
        "description": "REST architecture, HTTP methods, APIs, JSON, and CRUD concepts.",
    },
    {
        "name": "Backend Architecture",
        "slug": "backend-architecture",
        "description": "Core concepts used to design and structure backend applications.",
    },
    {
        "name": "Web Authentication",
        "slug": "web-authentication",
        "description": "Authentication, authorization, sessions, cookies, JWT, and OAuth.",
    },
    {
        "name": "Databases & ORM",
        "slug": "databases-orm",
        "description": "Database concepts, ORM, SQLAlchemy, relationships, and transactions.",
    },
    {
        "name": "Web Security",
        "slug": "web-security",
        "description": "Important security concepts for modern web applications.",
    },
    {
        "name": "Web Performance",
        "slug": "web-performance",
        "description": "Caching, optimization, compression, rate limiting, and scalability.",
    },
    {
        "name": "Testing & Debugging",
        "slug": "testing-debugging",
        "description": "Testing, debugging, pytest, mocking, and application quality.",
    },
    {
        "name": "Background Processing",
        "slug": "background-processing",
        "description": "Task queues, workers, Redis, Celery, and asynchronous processing.",
    },
    {
        "name": "Web Deployment",
        "slug": "web-deployment",
        "description": "Production deployment, Gunicorn, Nginx, configuration, and hosting.",
    },
    {
        "name": "Software Architecture",
        "slug": "software-architecture",
        "description": "Architecture patterns and principles for maintainable applications.",
    },
    {
        "name": "Python Web Ecosystem",
        "slug": "python-web-ecosystem",
        "description": "Python environments, packages, extensions, and web development tools.",
    },
]


# ============================================================
# HELPER
# ============================================================

def term(
    name,
    slug,
    definition,
    example,
    category_slug,
    level,
):
    return {
        "name": name,
        "slug": slug,
        "definition": definition,
        "example": example,
        "category_slug": category_slug,
        "level": level,
    }


# ============================================================
# GLOSSARY TERMS
# ============================================================

terms = [

    # ========================================================
    # 1. FLASK & MICROFRAMEWORKS
    # 21 TERMS
    # ========================================================

    term(
        "Flask",
        "flask",
        "Flask is a lightweight Python web framework used to build web applications and APIs.",
        "app = Flask(__name__)",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Jinja2",
        "jinja2",
        "Jinja2 is a template engine commonly used with Flask to generate dynamic HTML pages.",
        "<h1>{{ title }}</h1>",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Flask Route",
        "flask-route",
        "A Flask route connects a URL pattern to a Python view function.",
        "@app.route('/users')",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "View Function",
        "view-function",
        "A view function is a Python function that handles a web request and produces a response.",
        "def home(): return 'Hello'",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Flask Request",
        "flask-request",
        "The Flask request object provides information about the incoming HTTP request.",
        "request.args.get('name')",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Flask Response",
        "flask-response",
        "A Flask response represents the HTTP response returned to the client.",
        "return jsonify({'status': 'ok'})",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Blueprint",
        "blueprint",
        "A Blueprint organizes related Flask routes and application components into reusable modules.",
        "main_bp = Blueprint('main', __name__)",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Application Factory",
        "application-factory",
        "The application factory pattern creates a Flask application inside a function.",
        "def create_app(): return Flask(__name__)",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Flask Configuration",
        "flask-configuration",
        "Flask configuration stores application settings such as database URLs and secret keys.",
        "app.config['SECRET_KEY'] = '...' ",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Flask Context",
        "flask-context",
        "A Flask context provides information required while processing an application or request.",
        "with app.app_context():",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Application Context",
        "application-context",
        "The application context provides access to application-specific objects such as current_app.",
        "current_app.config",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Request Context",
        "request-context",
        "The request context contains request-specific information while Flask handles a request.",
        "request.method",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Error Handler",
        "error-handler",
        "An error handler allows Flask to return custom responses for specific HTTP errors or exceptions.",
        "@app.errorhandler(404)",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Custom CLI Command",
        "custom-cli-command",
        "A custom Flask CLI command adds project-specific commands to the Flask command-line interface.",
        "@app.cli.command('seed')",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Flask Extension",
        "flask-extension",
        "A Flask extension adds reusable functionality such as database integration, authentication, or caching.",
        "db = SQLAlchemy()",
        "flask-microframeworks",
        "Beginner",
    ),

    term(
        "Flask Middleware",
        "flask-middleware",
        "Middleware processes requests and responses around the Flask application.",
        "app.wsgi_app = middleware(app.wsgi_app)",
        "flask-microframeworks",
        "Advanced",
    ),

    term(
        "WSGI",
        "wsgi",
        "WSGI is a Python standard interface between web applications and web servers.",
        "Gunicorn communicates with Flask through WSGI.",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Flask Signals",
        "flask-signals",
        "Signals allow Flask extensions and applications to react to specific events without tightly coupling components.",
        "request_started.send(app)",
        "flask-microframeworks",
        "Advanced",
    ),

    term(
        "Streaming Response",
        "streaming-response",
        "A streaming response sends generated content progressively instead of constructing the entire response first.",
        "return Response(generate())",
        "flask-microframeworks",
        "Advanced",
    ),

    term(
        "Flask Testing Client",
        "flask-testing-client",
        "The Flask test client allows applications to simulate HTTP requests during automated testing.",
        "client.get('/')",
        "flask-microframeworks",
        "Moderate",
    ),

    term(
        "Application Dispatching",
        "application-dispatching",
        "Application dispatching allows multiple Flask applications or application components to be served through a common entry point.",
        "DispatcherMiddleware(app, apps)",
        "flask-microframeworks",
        "Advanced",
    ),


    # ========================================================
    # 2. REST APIs
    # 21 TERMS
    # ========================================================

    term(
        "REST",
        "rest",
        "REST is an architectural style for designing networked applications around resources.",
        "GET /api/users",
        "rest-apis",
        "Beginner",
    ),

    term(
        "API",
        "api",
        "An API is an interface that allows software systems to communicate with each other.",
        "GET /api/products",
        "rest-apis",
        "Beginner",
    ),

    term(
        "HTTP",
        "http",
        "HTTP is the protocol commonly used for communication between web clients and servers.",
        "GET /home HTTP/1.1",
        "rest-apis",
        "Beginner",
    ),

    term(
        "HTTP Method",
        "http-method",
        "An HTTP method describes the intended action of an HTTP request.",
        "GET, POST, PUT, PATCH, DELETE",
        "rest-apis",
        "Beginner",
    ),

    term(
        "GET",
        "get-method",
        "GET requests retrieve a resource or representation from a server.",
        "GET /api/users",
        "rest-apis",
        "Beginner",
    ),

    term(
        "POST",
        "post-method",
        "POST requests commonly submit data to create or process a resource.",
        "POST /api/users",
        "rest-apis",
        "Beginner",
    ),

    term(
        "PUT",
        "put-method",
        "PUT generally replaces or creates a resource at a specified URI.",
        "PUT /api/users/10",
        "rest-apis",
        "Beginner",
    ),

    term(
        "PATCH",
        "patch-method",
        "PATCH partially modifies an existing resource.",
        "PATCH /api/users/10",
        "rest-apis",
        "Beginner",
    ),

    term(
        "DELETE",
        "delete-method",
        "DELETE requests remove a resource.",
        "DELETE /api/users/10",
        "rest-apis",
        "Beginner",
    ),

    term(
        "JSON",
        "json",
        "JSON is a lightweight text format commonly used for exchanging structured data between clients and servers.",
        '{"name": "Charan"}',
        "rest-apis",
        "Beginner",
    ),

    term(
        "CRUD",
        "crud",
        "CRUD represents Create, Read, Update, and Delete operations on data.",
        "POST → Create, GET → Read",
        "rest-apis",
        "Beginner",
    ),

    term(
        "HTTP Status Code",
        "http-status-code",
        "An HTTP status code communicates the result of processing an HTTP request.",
        "200 OK",
        "rest-apis",
        "Beginner",
    ),

    term(
        "Query Parameter",
        "query-parameter",
        "A query parameter provides optional information in a URL.",
        "/users?page=2",
        "rest-apis",
        "Beginner",
    ),

    term(
        "Path Parameter",
        "path-parameter",
        "A path parameter identifies a resource within a URL path.",
        "/users/42",
        "rest-apis",
        "Beginner",
    ),

    term(
        "Request Body",
        "request-body",
        "The request body contains data sent by the client to the server.",
        '{"email": "user@example.com"}',
        "rest-apis",
        "Beginner",
    ),

    term(
        "Content Negotiation",
        "content-negotiation",
        "Content negotiation allows clients and servers to agree on the representation format of a resource.",
        "Accept: application/json",
        "rest-apis",
        "Moderate",
    ),

    term(
        "Idempotency",
        "idempotency",
        "An operation is idempotent when repeating the same request produces the same intended server state.",
        "PUT /users/10",
        "rest-apis",
        "Moderate",
    ),

    term(
        "Pagination",
        "api-pagination",
        "Pagination divides large collections of API results into smaller pages.",
        "/api/users?page=2&limit=20",
        "rest-apis",
        "Moderate",
    ),

    term(
        "API Versioning",
        "api-versioning",
        "API versioning allows different API contracts to coexist while clients migrate.",
        "/api/v1/users",
        "rest-apis",
        "Moderate",
    ),

    term(
        "HATEOAS",
        "hateoas",
        "HATEOAS allows API responses to include links that describe possible next actions.",
        '"links": [{"rel": "self", "href": "/users/1"}]',
        "rest-apis",
        "Advanced",
    ),

    term(
        "Rate Limit Headers",
        "rate-limit-headers",
        "Rate limit headers communicate request quotas and remaining capacity to API clients.",
        "X-RateLimit-Remaining: 42",
        "rest-apis",
        "Advanced",
    ),


    # ========================================================
    # 3. BACKEND ARCHITECTURE
    # 21 TERMS
    # ========================================================

    term(
        "Backend",
        "backend",
        "The backend is the server-side part of an application responsible for business logic, data access, and APIs.",
        "Flask handles the backend API.",
        "backend-architecture",
        "Beginner",
    ),

    term(
        "Route",
        "route",
        "A route maps an incoming URL and HTTP method to application logic.",
        "@app.route('/about')",
        "backend-architecture",
        "Beginner",
    ),

    term(
        "Controller",
        "controller",
        "A controller coordinates incoming requests with application logic and responses.",
        "UserController.get_user()",
        "backend-architecture",
        "Beginner",
    ),

    term(
        "Service Layer",
        "service-layer",
        "A service layer contains reusable business logic separately from request-handling code.",
        "user_service.create_user(data)",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Repository Pattern",
        "repository-pattern",
        "The repository pattern separates data-access operations from business logic.",
        "user_repository.find_by_id(1)",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Business Logic",
        "business-logic",
        "Business logic represents the rules and operations specific to an application's domain.",
        "Reject an order when stock is unavailable.",
        "backend-architecture",
        "Beginner",
    ),

    term(
        "Data Access Layer",
        "data-access-layer",
        "The data access layer handles communication between application logic and persistent storage.",
        "repository.save(user)",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Dependency Injection",
        "dependency-injection",
        "Dependency injection supplies required dependencies to components rather than making them construct those dependencies themselves.",
        "def service(repository): ...",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Inversion of Control",
        "inversion-of-control",
        "Inversion of control transfers responsibility for creating or coordinating dependencies to an external mechanism.",
        "A container provides a repository implementation.",
        "backend-architecture",
        "Advanced",
    ),

    term(
        "Separation of Concerns",
        "separation-of-concerns",
        "Separation of concerns keeps different responsibilities in distinct parts of an application.",
        "Routes handle HTTP while services handle business rules.",
        "backend-architecture",
        "Beginner",
    ),

    term(
        "DTO",
        "dto",
        "A Data Transfer Object carries structured data between application boundaries.",
        "UserCreateDTO(name, email)",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Schema",
        "backend-schema",
        "A schema defines the expected structure and validation rules of application data.",
        "UserSchema validates incoming user data.",
        "backend-architecture",
        "Beginner",
    ),

    term(
        "Serialization",
        "serialization",
        "Serialization converts application objects or data structures into a transferable representation.",
        "User object → JSON",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Deserialization",
        "deserialization",
        "Deserialization converts serialized data into an application representation.",
        "JSON → Python dictionary",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Application Boundary",
        "application-boundary",
        "An application boundary separates one responsibility or subsystem from another.",
        "API layer → service layer",
        "backend-architecture",
        "Advanced",
    ),

    term(
        "Domain Model",
        "domain-model",
        "A domain model represents important concepts and rules of a particular business domain.",
        "Order, Customer, Product",
        "backend-architecture",
        "Advanced",
    ),

    term(
        "Request Lifecycle",
        "request-lifecycle",
        "The request lifecycle describes the stages an HTTP request passes through before a response is returned.",
        "Request → middleware → route → response",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Middleware Chain",
        "middleware-chain",
        "A middleware chain is a sequence of processing components through which requests and responses pass.",
        "Authentication → logging → application",
        "backend-architecture",
        "Advanced",
    ),

    term(
        "Configuration Layer",
        "configuration-layer",
        "A configuration layer centralizes environment-specific application settings.",
        "Development and production configuration classes.",
        "backend-architecture",
        "Moderate",
    ),

    term(
        "Feature Module",
        "feature-module",
        "A feature module groups related backend functionality around a business capability.",
        "users/, orders/, payments/",
        "backend-architecture",
        "Advanced",
    ),

    term(
        "Backend Contract",
        "backend-contract",
        "A backend contract defines the expected interaction between an API and its consumers.",
        "OpenAPI specification defines endpoint behavior.",
        "backend-architecture",
        "Advanced",
    ),


    # ========================================================
    # 4. WEB AUTHENTICATION
    # 21 TERMS
    # ========================================================

    term(
        "Authentication",
        "authentication",
        "Authentication verifies the identity of a user or system.",
        "User logs in with email and password.",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Authorization",
        "authorization",
        "Authorization determines what an authenticated user or system is allowed to access.",
        "Only admins can delete users.",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Session",
        "session",
        "A session stores information associated with a user's interaction across requests.",
        "session['user_id'] = 10",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Cookie",
        "cookie",
        "A cookie is small data stored by a browser and sent with matching requests.",
        "Set-Cookie: session_id=abc",
        "web-authentication",
        "Beginner",
    ),

    term(
        "JWT",
        "jwt",
        "JSON Web Token is a compact token format commonly used to represent claims.",
        "Authorization: Bearer <token>",
        "web-authentication",
        "Moderate",
    ),

    term(
        "OAuth",
        "oauth",
        "OAuth is an authorization framework that allows applications to obtain limited access to resources.",
        "Sign in with an external identity provider.",
        "web-authentication",
        "Moderate",
    ),

    term(
        "OpenID Connect",
        "openid-connect",
        "OpenID Connect is an identity layer built on top of OAuth 2.0.",
        "An ID token describes the authenticated user.",
        "web-authentication",
        "Advanced",
    ),

    term(
        "Password Hashing",
        "password-hashing",
        "Password hashing transforms passwords into one-way representations suitable for secure storage.",
        "generate_password_hash(password)",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Password Salt",
        "password-salt",
        "A password salt is unique random data combined with a password before hashing.",
        "A hashing library generates a unique salt.",
        "web-authentication",
        "Moderate",
    ),

    term(
        "Access Token",
        "access-token",
        "An access token represents permission to access protected resources.",
        "Authorization: Bearer eyJ...",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Refresh Token",
        "refresh-token",
        "A refresh token can be exchanged for a new access token without requiring the user to authenticate again.",
        "POST /auth/refresh",
        "web-authentication",
        "Moderate",
    ),

    term(
        "Role-Based Access Control",
        "role-based-access-control",
        "RBAC grants permissions according to assigned user roles.",
        "admin → delete, editor → update",
        "web-authentication",
        "Moderate",
    ),

    term(
        "Permission",
        "permission",
        "A permission represents a specific action that an authenticated identity may perform.",
        "users.read",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Multi-Factor Authentication",
        "multi-factor-authentication",
        "MFA requires multiple independent authentication factors.",
        "Password + authenticator code",
        "web-authentication",
        "Moderate",
    ),

    term(
        "CSRF Token",
        "csrf-token",
        "A CSRF token helps a server verify that a state-changing request originated from an authorized application context.",
        "Hidden form field containing a CSRF token.",
        "web-authentication",
        "Moderate",
    ),

    term(
        "Bearer Token",
        "bearer-token",
        "A bearer token grants access to whoever presents the token successfully.",
        "Authorization: Bearer <token>",
        "web-authentication",
        "Beginner",
    ),

    term(
        "Token Expiration",
        "token-expiration",
        "Token expiration limits how long an authentication or authorization token remains valid.",
        "exp claim contains an expiration timestamp.",
        "web-authentication",
        "Moderate",
    ),

    term(
        "Single Sign-On",
        "single-sign-on",
        "Single Sign-On allows a user to authenticate once and access multiple connected applications.",
        "Company identity provider authenticates several internal applications.",
        "web-authentication",
        "Advanced",
    ),

    term(
        "Session Fixation",
        "session-fixation",
        "Session fixation is an attack where an attacker attempts to force a known session identifier onto a victim.",
        "Regenerate the session identifier after login.",
        "web-authentication",
        "Advanced",
    ),

    term(
        "PKCE",
        "pkce",
        "Proof Key for Code Exchange adds a code verifier mechanism to protect OAuth authorization-code flows.",
        "code_challenge is sent during authorization.",
        "web-authentication",
        "Advanced",
    ),

    term(
        "Identity Provider",
        "identity-provider",
        "An identity provider authenticates users and supplies identity information to applications.",
        "An enterprise identity provider issues authentication tokens.",
        "web-authentication",
        "Advanced",
    ),


    # ========================================================
    # 5. DATABASES & ORM
    # 21 TERMS
    # ========================================================

    term(
        "Database",
        "database",
        "A database stores and manages structured or unstructured application data.",
        "PostgreSQL stores application records.",
        "databases-orm",
        "Beginner",
    ),

    term(
        "SQL",
        "sql",
        "SQL is a language used to query and manage relational databases.",
        "SELECT * FROM users;",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Table",
        "database-table",
        "A table organizes relational database records into rows and columns.",
        "users(id, name, email)",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Primary Key",
        "primary-key",
        "A primary key uniquely identifies each row in a database table.",
        "id INTEGER PRIMARY KEY",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Foreign Key",
        "foreign-key",
        "A foreign key references a key in another table to establish a relationship.",
        "user_id REFERENCES users(id)",
        "databases-orm",
        "Beginner",
    ),

    term(
        "ORM",
        "orm",
        "Object-Relational Mapping allows developers to interact with relational database data using programming objects.",
        "User.query.filter_by(id=1).first()",
        "databases-orm",
        "Beginner",
    ),

    term(
        "SQLAlchemy",
        "sqlalchemy",
        "SQLAlchemy is a Python SQL toolkit and Object-Relational Mapper.",
        "class User(db.Model):",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Model",
        "database-model",
        "A model represents application data and commonly maps to a database table.",
        "class User(db.Model):",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Migration",
        "database-migration",
        "A database migration records controlled changes to a database schema.",
        "Add an email column through a migration.",
        "databases-orm",
        "Moderate",
    ),

    term(
        "Transaction",
        "database-transaction",
        "A transaction groups database operations into a unit that can be committed or rolled back.",
        "db.session.commit()",
        "databases-orm",
        "Moderate",
    ),

    term(
        "Commit",
        "database-commit",
        "A commit permanently applies pending database transaction changes.",
        "db.session.commit()",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Rollback",
        "database-rollback",
        "A rollback reverses uncommitted changes in the current transaction.",
        "db.session.rollback()",
        "databases-orm",
        "Beginner",
    ),

    term(
        "Database Index",
        "database-index",
        "An index improves lookup performance for selected database columns.",
        "CREATE INDEX idx_email ON users(email);",
        "databases-orm",
        "Moderate",
    ),

    term(
        "One-to-Many Relationship",
        "one-to-many-relationship",
        "A one-to-many relationship connects one record to multiple related records.",
        "One author → many books",
        "databases-orm",
        "Moderate",
    ),

    term(
        "Many-to-Many Relationship",
        "many-to-many-relationship",
        "A many-to-many relationship connects multiple records on both sides through an association structure.",
        "Students ↔ Courses",
        "databases-orm",
        "Moderate",
    ),

term(
    "ORM Relationship Loading",
    "orm-relationship-loading",
    "ORM relationship loading controls how related database objects are retrieved when working with mapped models.",
    "Configure a relationship to load related records only when needed.",
    "databases-orm",
    "Moderate",
),

    term(
        "Eager Loading",
        "eager-loading",
        "Eager loading retrieves related data as part of the initial database operation.",
        "joinedload(User.orders)",
        "databases-orm",
        "Advanced",
    ),

    term(
        "N+1 Query Problem",
        "n-plus-one-query-problem",
        "The N+1 query problem occurs when an application performs one query for a collection and additional queries for each related record.",
        "One users query followed by one orders query per user.",
        "databases-orm",
        "Advanced",
    ),

    term(
        "Connection Pool",
        "database-connection-pool",
        "A connection pool manages reusable database connections to reduce connection setup overhead.",
        "SQLAlchemy maintains pooled connections.",
        "databases-orm",
        "Advanced",
    ),

    term(
        "Isolation Level",
        "transaction-isolation-level",
        "A transaction isolation level controls how concurrent transactions interact with each other's changes.",
        "READ COMMITTED",
        "databases-orm",
        "Advanced",
    ),

    term(
        "Database Normalization",
        "database-normalization",
        "Database normalization organizes relational data to reduce unnecessary duplication and update anomalies.",
        "Separate customers and orders into related tables.",
        "databases-orm",
        "Moderate",
    ),


    # ========================================================
    # 6. WEB SECURITY
    # 21 TERMS
    # ========================================================

    term(
        "Web Security",
        "web-security",
        "Web security is the practice of protecting web applications, users, data, and infrastructure from attacks.",
        "Validate input before processing it.",
        "web-security",
        "Beginner",
    ),

    term(
        "XSS",
        "xss",
        "Cross-Site Scripting occurs when untrusted content is interpreted as executable script in a user's browser.",
        "Escape untrusted HTML content.",
        "web-security",
        "Beginner",
    ),

    term(
        "SQL Injection",
        "sql-injection",
        "SQL injection occurs when untrusted input changes the meaning of a database query.",
        "Use parameterized queries instead of string concatenation.",
        "web-security",
        "Beginner",
    ),

    term(
        "CSRF",
        "csrf",
        "Cross-Site Request Forgery tricks an authenticated browser into sending an unintended state-changing request.",
        "Use CSRF tokens on protected forms.",
        "web-security",
        "Beginner",
    ),

    term(
        "CORS",
        "cors",
        "Cross-Origin Resource Sharing controls which origins may access resources from a different origin.",
        "Access-Control-Allow-Origin",
        "web-security",
        "Beginner",
    ),

    term(
        "HTTPS",
        "https",
        "HTTPS protects HTTP communication using TLS encryption.",
        "https://example.com",
        "web-security",
        "Beginner",
    ),

    term(
        "TLS",
        "tls",
        "TLS provides encryption, integrity, and authentication for network communication.",
        "HTTPS uses TLS.",
        "web-security",
        "Moderate",
    ),

    term(
        "Content Security Policy",
        "content-security-policy",
        "CSP is a browser security mechanism that restricts which resources a page may load or execute.",
        "Content-Security-Policy: default-src 'self'",
        "web-security",
        "Moderate",
    ),

    term(
        "Security Headers",
        "security-headers",
        "Security headers communicate browser security policies through HTTP response headers.",
        "X-Content-Type-Options: nosniff",
        "web-security",
        "Beginner",
    ),

    term(
        "Clickjacking",
        "clickjacking",
        "Clickjacking tricks users into interacting with hidden or disguised interface elements.",
        "Use frame-ancestors in CSP.",
        "web-security",
        "Moderate",
    ),

    term(
        "Input Validation",
        "input-validation",
        "Input validation checks incoming data against expected rules before processing it.",
        "Validate that age is an integer.",
        "web-security",
        "Beginner",
    ),

    term(
        "Output Encoding",
        "output-encoding",
        "Output encoding converts data into a safe representation for its destination context.",
        "HTML-escape user-generated content.",
        "web-security",
        "Moderate",
    ),

    term(
        "Secrets Management",
        "secrets-management",
        "Secrets management protects sensitive values such as API keys and database passwords.",
        "Store secrets in environment variables or a secret manager.",
        "web-security",
        "Moderate",
    ),

    term(
        "Brute Force Attack",
        "brute-force-attack",
        "A brute force attack repeatedly tries possible credentials or values until a valid one is found.",
        "Rate-limit repeated login attempts.",
        "web-security",
        "Beginner",
    ),

    term(
        "Rate Limiting",
        "security-rate-limiting",
        "Rate limiting restricts how frequently a client can perform an operation.",
        "Allow 100 requests per minute.",
        "web-security",
        "Moderate",
    ),

    term(
        "Secure Cookie",
        "secure-cookie",
        "A secure cookie uses browser cookie attributes that reduce exposure during transmission or client-side access.",
        "Secure; HttpOnly; SameSite",
        "web-security",
        "Moderate",
    ),

    term(
        "HttpOnly Cookie",
        "httponly-cookie",
        "The HttpOnly attribute prevents client-side JavaScript from directly reading a cookie.",
        "Set-Cookie: session=abc; HttpOnly",
        "web-security",
        "Beginner",
    ),

    term(
        "SameSite Cookie",
        "samesite-cookie",
        "The SameSite cookie attribute controls whether cookies are sent with cross-site requests.",
        "SameSite=Lax",
        "web-security",
        "Moderate",
    ),

    term(
        "Threat Modeling",
        "threat-modeling",
        "Threat modeling systematically identifies assets, threats, vulnerabilities, and mitigations.",
        "Identify attack paths for an authentication system.",
        "web-security",
        "Advanced",
    ),

    term(
        "Security Misconfiguration",
        "security-misconfiguration",
        "Security misconfiguration occurs when applications or infrastructure use unsafe or unnecessary settings.",
        "Leaving debug mode enabled in production.",
        "web-security",
        "Moderate",
    ),

    term(
        "Defense in Depth",
        "defense-in-depth",
        "Defense in depth uses multiple independent security controls so that one failure does not expose the entire system.",
        "Authentication + authorization + validation + monitoring.",
        "web-security",
        "Advanced",
    ),


    # ========================================================
    # 7. WEB PERFORMANCE
    # 21 TERMS
    # ========================================================

    term(
        "Caching",
        "caching",
        "Caching stores frequently accessed data temporarily so future requests can be served faster.",
        "Cache frequently requested API results.",
        "web-performance",
        "Beginner",
    ),

    term(
        "Browser Cache",
        "browser-cache",
        "A browser cache stores reusable web resources locally on the client.",
        "Cache CSS and JavaScript files.",
        "web-performance",
        "Beginner",
    ),

    term(
        "HTTP Cache",
        "http-cache",
        "HTTP caching uses response headers to control how clients and intermediaries store responses.",
        "Cache-Control: max-age=3600",
        "web-performance",
        "Moderate",
    ),

    term(
        "Compression",
        "compression",
        "Compression reduces the size of data transferred between servers and clients.",
        "gzip or Brotli compression",
        "web-performance",
        "Beginner",
    ),

    term(
        "Lazy Loading",
        "web-lazy-loading",
        "Lazy loading delays loading resources until they are needed.",
        "Load an image when it enters the viewport.",
        "web-performance",
        "Beginner",
    ),

    term(
        "Pagination Performance",
        "pagination-performance",
        "Pagination limits the amount of data returned or rendered in one request.",
        "Return 20 records per API page.",
        "web-performance",
        "Beginner",
    ),

    term(
        "Database Query Optimization",
        "database-query-optimization",
        "Query optimization reduces unnecessary database work and improves response times.",
        "Add an index for frequent lookups.",
        "web-performance",
        "Moderate",
    ),

    term(
        "Connection Reuse",
        "connection-reuse",
        "Connection reuse avoids repeatedly establishing network or database connections.",
        "Reuse pooled database connections.",
        "web-performance",
        "Moderate",
    ),

    term(
        "CDN",
        "cdn",
        "A Content Delivery Network distributes cached content across geographically distributed servers.",
        "Serve static assets through a CDN.",
        "web-performance",
        "Beginner",
    ),

    term(
        "Reverse Proxy",
        "reverse-proxy",
        "A reverse proxy receives client requests and forwards them to backend services.",
        "Nginx forwards requests to Gunicorn.",
        "web-performance",
        "Moderate",
    ),

    term(
        "Load Balancing",
        "load-balancing",
        "Load balancing distributes incoming traffic across multiple application instances.",
        "Requests distributed across three servers.",
        "web-performance",
        "Moderate",
    ),

term(
    "Resource Throttling",
    "resource-throttling",
    "Resource throttling deliberately limits the rate at which a system processes work to protect available resources.",
    "Limit expensive operations when server resources become constrained.",
    "web-performance",
    "Moderate",
),

    term(
        "Debouncing",
        "debouncing",
        "Debouncing delays execution until a burst of events has stopped.",
        "Wait 300ms before sending a search request.",
        "web-performance",
        "Moderate",
    ),

    term(
        "Throttling",
        "throttling",
        "Throttling limits how frequently an operation can execute during a period.",
        "Process scroll events at most once every 100ms.",
        "web-performance",
        "Moderate",
    ),

    term(
        "Response Time",
        "response-time",
        "Response time is the elapsed time between a request and the corresponding response.",
        "API responds in 120ms.",
        "web-performance",
        "Beginner",
    ),

    term(
        "Throughput",
        "throughput",
        "Throughput measures how much work a system completes over a period.",
        "Requests per second.",
        "web-performance",
        "Moderate",
    ),

    term(
        "Latency",
        "latency",
        "Latency measures the delay involved in completing a request or operation.",
        "Network latency is 40ms.",
        "web-performance",
        "Beginner",
    ),

    term(
        "Cache Invalidation",
        "cache-invalidation",
        "Cache invalidation removes or refreshes stale cached data when the underlying data changes.",
        "Delete a product cache entry after an update.",
        "web-performance",
        "Advanced",
    ),

    term(
        "Cache Stampede",
        "cache-stampede",
        "A cache stampede occurs when many requests simultaneously regenerate an expired cached value.",
        "Several requests query the database after cache expiration.",
        "web-performance",
        "Advanced",
    ),

    term(
        "Horizontal Scaling",
        "horizontal-scaling",
        "Horizontal scaling increases capacity by adding more application instances.",
        "Run five API servers instead of one.",
        "web-performance",
        "Advanced",
    ),

    term(
        "Vertical Scaling",
        "vertical-scaling",
        "Vertical scaling increases the resources of an existing server.",
        "Increase server memory from 8GB to 16GB.",
        "web-performance",
        "Moderate",
    ),


    # ========================================================
    # 8. TESTING & DEBUGGING
    # 21 TERMS
    # ========================================================

    term(
        "Testing",
        "testing",
        "Testing verifies that software behaves according to expected requirements.",
        "Run automated tests before deployment.",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Unit Testing",
        "unit-testing",
        "Unit testing verifies individual units of application code in isolation.",
        "def test_add(): assert add(2, 3) == 5",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Integration Testing",
        "integration-testing",
        "Integration testing verifies that multiple application components work together correctly.",
        "Test an API endpoint with a test database.",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "End-to-End Testing",
        "end-to-end-testing",
        "End-to-end testing verifies a complete user or system workflow.",
        "Login → dashboard → logout.",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "Pytest",
        "pytest",
        "Pytest is a Python testing framework commonly used for automated tests.",
        "pytest tests/",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Assertion",
        "assertion",
        "An assertion checks whether an actual result matches an expected condition.",
        "assert response.status_code == 200",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Fixture",
        "pytest-fixture",
        "A pytest fixture provides reusable setup or data for tests.",
        "@pytest.fixture",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "Mocking",
        "mocking",
        "Mocking replaces a real dependency with a controlled test double.",
        "Mock an external API during a unit test.",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "Monkeypatching",
        "monkeypatching",
        "Monkeypatching temporarily replaces objects or behavior during testing.",
        "monkeypatch.setattr(module, 'API_URL', test_url)",
        "testing-debugging",
        "Advanced",
    ),

    term(
        "Test Coverage",
        "test-coverage",
        "Test coverage measures how much application code is exercised by tests.",
        "pytest --cov=app",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Regression Testing",
        "regression-testing",
        "Regression testing verifies that existing behavior remains correct after changes.",
        "Run the existing test suite after a refactor.",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "Test Double",
        "test-double",
        "A test double is a substitute object used to isolate code under test.",
        "Stub, fake, mock, or spy.",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "Stub",
        "stub",
        "A stub provides predefined responses to support a test.",
        "Return a fixed user object from a stub.",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Spy",
        "spy",
        "A spy records how a dependency was called so the test can inspect those interactions.",
        "Verify that send_email() was called once.",
        "testing-debugging",
        "Moderate",
    ),

    term(
        "Debugging",
        "debugging",
        "Debugging is the process of finding and correcting software defects.",
        "Inspect a traceback to locate an exception.",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Traceback",
        "traceback",
        "A traceback shows the sequence of calls that led to a Python exception.",
        "Read the file and line number from the traceback.",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Logging",
        "logging",
        "Logging records application events that help developers understand system behavior.",
        "app.logger.info('User logged in')",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Breakpoint",
        "breakpoint",
        "A breakpoint pauses program execution so developers can inspect program state.",
        "breakpoint()",
        "testing-debugging",
        "Beginner",
    ),

    term(
        "Property-Based Testing",
        "property-based-testing",
        "Property-based testing generates many inputs to verify that general properties remain true.",
        "Test that sorting always produces ordered output.",
        "testing-debugging",
        "Advanced",
    ),

    term(
        "Contract Testing",
        "contract-testing",
        "Contract testing verifies that communicating services agree on an expected interface.",
        "Verify an API response matches the consumer contract.",
        "testing-debugging",
        "Advanced",
    ),

    term(
        "Test Isolation",
        "test-isolation",
        "Test isolation ensures one test does not unexpectedly depend on another test's state.",
        "Use a fresh database transaction for each test.",
        "testing-debugging",
        "Moderate",
    ),


    # ========================================================
    # 9. BACKGROUND PROCESSING
    # 21 TERMS
    # ========================================================

    term(
        "Background Task",
        "background-task",
        "A background task performs work outside the main request-response cycle.",
        "Generate a report after returning the HTTP response.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Task Queue",
        "task-queue",
        "A task queue stores work items that workers process asynchronously.",
        "Add email sending to a queue.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Worker",
        "background-worker",
        "A worker is a process that consumes and executes queued tasks.",
        "Celery worker processes queued jobs.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Celery",
        "celery",
        "Celery is a distributed task queue commonly used with Python applications.",
        "celery -A app worker",
        "background-processing",
        "Beginner",
    ),

    term(
        "Redis",
        "redis",
        "Redis is an in-memory data store commonly used for caching and task queues.",
        "Redis stores Celery broker messages.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Message Broker",
        "message-broker",
        "A message broker receives and distributes messages between producers and consumers.",
        "Redis or RabbitMQ can act as a broker.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Producer",
        "task-producer",
        "A producer creates messages or tasks and sends them to a queue or broker.",
        "A Flask endpoint submits a Celery task.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Consumer",
        "task-consumer",
        "A consumer receives and processes messages from a queue.",
        "A worker consumes queued tasks.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Task Retry",
        "task-retry",
        "Task retrying allows failed background work to be attempted again.",
        "Retry an email task after a temporary SMTP error.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Task Timeout",
        "task-timeout",
        "A task timeout stops or marks a task as failed after a specified period.",
        "Stop a task after 30 seconds.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Scheduled Task",
        "scheduled-task",
        "A scheduled task executes automatically at a specified time or interval.",
        "Run a cleanup job every night.",
        "background-processing",
        "Beginner",
    ),

    term(
        "Celery Beat",
        "celery-beat",
        "Celery Beat schedules periodic Celery tasks.",
        "Run cleanup.s() every hour.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Task Result Backend",
        "task-result-backend",
        "A result backend stores the status or result of asynchronous tasks.",
        "Store task results in Redis.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Task Idempotency",
        "task-idempotency",
        "An idempotent task can safely be executed more than once without producing unintended repeated effects.",
        "Use a unique payment operation ID.",
        "background-processing",
        "Advanced",
    ),

    term(
        "Dead Letter Queue",
        "dead-letter-queue",
        "A dead letter queue stores messages that cannot be successfully processed.",
        "Move repeatedly failed jobs to a DLQ.",
        "background-processing",
        "Advanced",
    ),

    term(
        "Worker Pool",
        "worker-pool",
        "A worker pool maintains multiple worker processes or threads for concurrent task execution.",
        "Four workers process independent jobs.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Task Priority",
        "task-priority",
        "Task priority determines which queued tasks should be processed before others.",
        "Critical notifications receive higher priority.",
        "background-processing",
        "Moderate",
    ),

    term(
        "Backpressure",
        "backpressure",
        "Backpressure slows or limits producers when consumers cannot keep up with incoming work.",
        "Limit queue intake when workers are overloaded.",
        "background-processing",
        "Advanced",
    ),

    term(
        "Distributed Task",
        "distributed-task",
        "A distributed task can be processed by workers running across multiple machines or processes.",
        "Workers on several servers process the same queue.",
        "background-processing",
        "Advanced",
    ),

    term(
        "Task Chaining",
        "task-chaining",
        "Task chaining executes multiple background tasks in a defined sequence.",
        "Resize image → generate thumbnail → notify user.",
        "background-processing",
        "Advanced",
    ),

    term(
        "Task Monitoring",
        "task-monitoring",
        "Task monitoring tracks queued, running, completed, and failed background jobs.",
        "Monitor Celery worker task states.",
        "background-processing",
        "Moderate",
    ),


    # ========================================================
    # 10. WEB DEPLOYMENT
    # 21 TERMS
    # ========================================================

    term(
        "Deployment",
        "deployment",
        "Deployment is the process of making an application available in a target environment.",
        "Deploy a Flask application to a cloud host.",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Production Environment",
        "production-environment",
        "The production environment hosts the version of an application used by real users.",
        "FLASK_ENV-like development settings should not be used as production configuration.",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Development Environment",
        "development-environment",
        "A development environment is configured for building, testing, and debugging software.",
        "Run Flask locally with development settings.",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Environment Variable",
        "environment-variable",
        "Environment variables provide configuration values outside application source code.",
        "DATABASE_URL=postgresql://...",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Gunicorn",
        "gunicorn",
        "Gunicorn is a Python WSGI HTTP server commonly used to serve Python applications in production.",
        "gunicorn run:app",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Nginx",
        "nginx",
        "Nginx is a web server and reverse proxy commonly placed in front of application servers.",
        "Nginx → Gunicorn → Flask",
        "web-deployment",
        "Beginner",
    ),

    term(
        "WSGI Server",
        "wsgi-server",
        "A WSGI server runs Python web applications according to the WSGI interface.",
        "Gunicorn serves a Flask application.",
        "web-deployment",
        "Moderate",
    ),

    term(
        "ASGI",
        "asgi",
        "ASGI is an interface for Python web applications supporting asynchronous capabilities.",
        "An ASGI server can run async Python web applications.",
        "web-deployment",
        "Moderate",
    ),

term(
    "Edge Server",
    "edge-server",
    "An edge server handles requests close to clients and can provide functions such as caching, routing, and content delivery.",
    "A CDN edge server returns a cached static asset.",
    "web-performance",
    "Advanced",
),

    term(
        "Domain Name",
        "domain-name",
        "A domain name provides a human-readable address for accessing a web application.",
        "example.com",
        "web-deployment",
        "Beginner",
    ),

    term(
        "DNS",
        "dns",
        "DNS translates domain names into network addresses and other resource records.",
        "example.com → server address",
        "web-deployment",
        "Beginner",
    ),

    term(
        "SSL Certificate",
        "ssl-certificate",
        "A TLS certificate helps authenticate a website and enables encrypted HTTPS communication.",
        "Certificate issued for example.com.",
        "web-deployment",
        "Beginner",
    ),

    term(
        "CI/CD",
        "ci-cd",
        "CI/CD automates software integration, testing, and delivery or deployment workflows.",
        "Push code → run tests → deploy.",
        "web-deployment",
        "Moderate",
    ),

    term(
        "Build Pipeline",
        "build-pipeline",
        "A build pipeline automates steps required to transform source code into a deployable artifact.",
        "Install dependencies → test → package.",
        "web-deployment",
        "Moderate",
    ),

    term(
        "Health Check",
        "health-check",
        "A health check endpoint or mechanism indicates whether an application is operating correctly.",
        "GET /health → 200 OK",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Zero-Downtime Deployment",
        "zero-downtime-deployment",
        "Zero-downtime deployment updates an application while minimizing interruption for users.",
        "Run new instances before removing old instances.",
        "web-deployment",
        "Advanced",
    ),

    term(
        "Blue-Green Deployment",
        "blue-green-deployment",
        "Blue-green deployment maintains two environments and switches traffic between them during releases.",
        "Blue = current, Green = new.",
        "web-deployment",
        "Advanced",
    ),

    term(
        "Rolling Deployment",
        "rolling-deployment",
        "A rolling deployment updates application instances gradually instead of replacing all instances simultaneously.",
        "Update two instances at a time.",
        "web-deployment",
        "Advanced",
    ),

    term(
        "Containerization",
        "containerization",
        "Containerization packages an application and its dependencies into an isolated runtime environment.",
        "Docker image containing the Flask app.",
        "web-deployment",
        "Moderate",
    ),

    term(
        "Docker Image",
        "docker-image",
        "A Docker image is a packaged filesystem and metadata used to create containers.",
        "docker build -t flask-app .",
        "web-deployment",
        "Beginner",
    ),

    term(
        "Infrastructure as Code",
        "infrastructure-as-code",
        "Infrastructure as Code defines infrastructure configuration using version-controlled files.",
        "Terraform configuration defines cloud resources.",
        "web-deployment",
        "Advanced",
    ),


    # ========================================================
    # 11. SOFTWARE ARCHITECTURE
    # 20 TERMS
    # ========================================================

    term(
        "MVC",
        "mvc",
        "Model-View-Controller separates application data, presentation, and request handling responsibilities.",
        "Model → Data, View → UI, Controller → Request handling.",
        "software-architecture",
        "Beginner",
    ),

    term(
        "Layered Architecture",
        "layered-architecture",
        "Layered architecture organizes software into logical layers with distinct responsibilities.",
        "Presentation → Service → Data Access",
        "software-architecture",
        "Beginner",
    ),

    term(
        "Monolithic Architecture",
        "monolithic-architecture",
        "A monolithic application is deployed as a single application unit.",
        "One Flask application containing all modules.",
        "software-architecture",
        "Beginner",
    ),

    term(
        "Microservices",
        "microservices",
        "Microservices architecture divides an application into independently deployable services.",
        "User service and payment service run separately.",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Modular Monolith",
        "modular-monolith",
        "A modular monolith is a single deployable application organized into well-defined internal modules.",
        "Users and orders are separate modules in one application.",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Clean Architecture",
        "clean-architecture",
        "Clean Architecture separates business rules from external frameworks and infrastructure.",
        "Domain → use cases → adapters → infrastructure.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "Hexagonal Architecture",
        "hexagonal-architecture",
        "Hexagonal architecture separates core application logic from external systems through ports and adapters.",
        "Database adapter implements a repository port.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "Domain-Driven Design",
        "domain-driven-design",
        "Domain-Driven Design structures software around domain concepts and business rules.",
        "Order aggregate represents ordering rules.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "SOLID",
        "solid",
        "SOLID is a group of object-oriented design principles intended to support maintainable software.",
        "Single Responsibility Principle.",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Single Responsibility Principle",
        "single-responsibility-principle",
        "A component should have a focused responsibility and a reason to change.",
        "Separate email sending from user registration.",
        "software-architecture",
        "Beginner",
    ),

    term(
        "Open-Closed Principle",
        "open-closed-principle",
        "The Open-Closed Principle encourages software components to be open for extension but closed for unnecessary modification.",
        "Add a new payment strategy without rewriting the checkout flow.",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Dependency Inversion Principle",
        "dependency-inversion-principle",
        "The Dependency Inversion Principle encourages high-level logic to depend on abstractions rather than concrete implementations.",
        "Service depends on a repository interface.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "Facade Pattern",
        "facade-pattern",
        "The Facade pattern provides a simplified interface over a more complex subsystem.",
        "OrderService exposes one method for checkout.",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Factory Pattern",
        "factory-pattern",
        "The Factory pattern centralizes object creation so callers do not need to know construction details.",
        "PaymentFactory.create('stripe')",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Strategy Pattern",
        "strategy-pattern",
        "The Strategy pattern allows interchangeable algorithms behind a common interface.",
        "Different payment strategies implement pay().",
        "software-architecture",
        "Advanced",
    ),

    term(
        "Observer Pattern",
        "observer-pattern",
        "The Observer pattern allows objects to receive notifications when another object changes state.",
        "Listeners react to an order-created event.",
        "software-architecture",
        "Moderate",
    ),

    term(
        "Event-Driven Architecture",
        "event-driven-architecture",
        "Event-driven architecture uses events to communicate that something has happened in a system.",
        "OrderCreated event triggers notification processing.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "CQRS",
        "cqrs",
        "Command Query Responsibility Segregation separates operations that change state from operations that read state.",
        "Commands write data while queries read optimized views.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "API Gateway",
        "api-gateway",
        "An API gateway provides a common entry point for clients accessing multiple backend services.",
        "Gateway routes requests to user and order services.",
        "software-architecture",
        "Advanced",
    ),

    term(
        "Circuit Breaker",
        "circuit-breaker",
        "The circuit breaker pattern temporarily stops calls to an unhealthy dependency to prevent cascading failures.",
        "Stop calling a failing payment service for a short period.",
        "software-architecture",
        "Advanced",
    ),


    # ========================================================
    # 12. PYTHON WEB ECOSYSTEM
    # 20 TERMS
    # ========================================================

    term(
        "Python",
        "python",
        "Python is a general-purpose programming language widely used for web development and backend systems.",
        "print('Hello, Python')",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "Virtual Environment",
        "virtual-environment",
        "A Python virtual environment isolates project dependencies from other Python projects.",
        "python -m venv venv",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "pip",
        "pip",
        "pip is the standard package installer commonly used to install Python packages.",
        "pip install flask",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "requirements.txt",
        "requirements-txt",
        "requirements.txt records Python package dependencies for a project.",
        "pip install -r requirements.txt",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "pyproject.toml",
        "pyproject-toml",
        "pyproject.toml is a standardized configuration file used by Python projects and packaging tools.",
        "[project]",
        "python-web-ecosystem",
        "Moderate",
    ),

    term(
        "Package",
        "python-package",
        "A Python package groups reusable Python modules and related project files.",
        "import requests",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "Module",
        "python-module",
        "A Python module is a file containing Python code that can be imported into another module.",
        "from utils import helper",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "Import",
        "python-import",
        "An import statement makes definitions from another module available to Python code.",
        "from flask import Flask",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "Virtualenv",
        "virtualenv",
        "virtualenv is a tool for creating isolated Python environments.",
        "virtualenv .venv",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "Poetry",
        "poetry",
        "Poetry is a Python dependency-management and packaging tool.",
        "poetry add flask",
        "python-web-ecosystem",
        "Moderate",
    ),

    term(
        "Pipenv",
        "pipenv",
        "Pipenv combines dependency management and virtual environment workflows for Python projects.",
        "pipenv install flask",
        "python-web-ecosystem",
        "Moderate",
    ),

    term(
        "Uvicorn",
        "uvicorn",
        "Uvicorn is an ASGI server commonly used to run asynchronous Python web applications.",
        "uvicorn main:app",
        "python-web-ecosystem",
        "Moderate",
    ),

 term(
    "WSGI Application Object",
    "wsgi-application-object",
    "A WSGI application object is a Python callable that receives a WSGI environment and returns an HTTP response through the WSGI interface.",
    "A Flask application can be exposed as the WSGI application object.",
    "python-web-ecosystem",
    "Advanced",
),

    term(
        "Requests",
        "requests-library",
        "Requests is a Python HTTP client library used to make HTTP requests.",
        "requests.get('https://example.com')",
        "python-web-ecosystem",
        "Beginner",
    ),

    term(
        "httpx",
        "httpx",
        "httpx is a Python HTTP client supporting both synchronous and asynchronous requests.",
        "httpx.get(url)",
        "python-web-ecosystem",
        "Moderate",
    ),

    term(
        "Pydantic",
        "pydantic",
        "Pydantic validates and parses data using Python type annotations and models.",
        "class User(BaseModel): ...",
        "python-web-ecosystem",
        "Moderate",
    ),

    term(
        "Marshmallow",
        "marshmallow",
        "Marshmallow is a Python library used for serializing, deserializing, and validating data.",
        "UserSchema().load(data)",
        "python-web-ecosystem",
        "Moderate",
    ),

    term(
        "Alembic",
        "alembic",
        "Alembic is a database migration tool commonly used with SQLAlchemy.",
        "alembic upgrade head",
        "python-web-ecosystem",
        "Advanced",
    ),

    term(
        "Gunicorn Worker Model",
        "gunicorn-worker-model",
        "Gunicorn can run multiple worker processes to handle concurrent application requests.",
        "gunicorn --workers 4 app:app",
        "python-web-ecosystem",
        "Advanced",
    ),

    term(
        "Python Packaging",
        "python-packaging",
        "Python packaging defines how reusable Python software is structured, built, distributed, and installed.",
        "Build a wheel and publish a package.",
        "python-web-ecosystem",
        "Advanced",
    ),
]


# ============================================================
# VALIDATION
# ============================================================

def validate_terms():
    expected_count = 250

    if len(terms) != expected_count:
        raise ValueError(
            f"Expected {expected_count} terms, found {len(terms)}."
        )

    names = [item["name"] for item in terms]
    slugs = [item["slug"] for item in terms]

    if len(names) != len(set(names)):
        raise ValueError("Duplicate glossary term names detected.")

    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate glossary term slugs detected.")

    valid_levels = {
        "Beginner",
        "Moderate",
        "Advanced",
    }

    for item in terms:
        if item["level"] not in valid_levels:
            raise ValueError(
                f"Invalid level for {item['name']}: {item['level']}"
            )

    category_counts = {}

    for item in terms:
        category = item["category_slug"]
        category_counts[category] = category_counts.get(category, 0) + 1

    if len(category_counts) != 12:
        raise ValueError(
            f"Expected 12 categories, found {len(category_counts)}."
        )

    level_counts = {}

    for item in terms:
        level = item["level"]
        level_counts[level] = level_counts.get(level, 0) + 1

    print("Term count:", len(terms))
    print("Category counts:")

    for category, count in category_counts.items():
        print(f"  {category}: {count}")

    print("Level counts:")

    for level, count in level_counts.items():
        print(f"  {level}: {count}")


# ============================================================
# SEED DATABASE
# ============================================================

def seed_categories():
    validate_terms()

    app = create_app()

    with app.app_context():

        # ----------------------------------------
        # Seed categories
        # ----------------------------------------

        for category_data in categories:

            existing_category = Category.query.filter_by(
                slug=category_data["slug"]
            ).first()

            if existing_category:
                continue

            category = Category(**category_data)

            db.session.add(category)

        db.session.commit()

        # ----------------------------------------
        # Seed glossary terms
        # ----------------------------------------

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
                level=term_data["level"],
                category_id=category.id,
            )

            db.session.add(glossary_term)

        db.session.commit()

        print()
        print("=" * 60)
        print("Tech Glossary Hub — Flask")
        print("=" * 60)
        print("Categories seeded successfully.")
        print("Glossary terms seeded successfully.")
        print(f"Total glossary terms: {len(terms)}")
        print("=" * 60)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    seed_categories()