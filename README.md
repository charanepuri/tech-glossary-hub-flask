# 📚 Tech Glossary Hub — Flask

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Vercel](https://img.shields.io/badge/Vercel-Deployment-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

> A modern technical glossary web application built with **Flask, SQLAlchemy, SQLite, HTML, CSS, and JavaScript**, designed to provide a structured and searchable collection of backend and Python web-development terminology.

---

## 📌 Project Overview

**Tech Glossary Hub — Flask** is the Flask edition of the **Tech Glossary Hub** project series.

The application focuses primarily on backend and Python web-development concepts, including:

- Flask & Microframeworks
- REST APIs
- Backend Architecture
- Web Authentication
- Databases & ORM
- Web Security
- Web Performance
- Testing & Debugging
- Background Processing
- Web Deployment
- Software Architecture
- Python Web Ecosystem

The application contains **250 glossary terms across 12 technical categories**, with each term organized according to its category and learning level.

It provides a developer-oriented interface with:

- Search
- Category filtering
- Pagination
- Detailed term pages
- Related terms
- Previous/next term navigation
- Multiple project-version navigation

---

## ✨ Features

### 📚 Technical Glossary

- **250 technical terms**
- **12 technical categories**
- Beginner, Moderate, and Advanced learning levels
- Individual term detail pages
- Definitions
- Practical examples
- Related terms
- Previous and next term navigation

### 🔎 Search & Filtering

The glossary supports:

- Search terms by name
- Search definitions
- Search examples
- Filter terms by category
- Combined search and category filtering
- Clear active filters

### 📄 Pagination

Pagination keeps the glossary interface clean and easy to navigate.

Features include:

- Previous page
- Next page
- Page numbers
- Current page indicator
- Result information

### 🗂️ Category System

Each glossary term belongs to one of the following **12 categories**:

|   # | Category                |
| --: | ----------------------- |
|   1 | Flask & Microframeworks |
|   2 | REST APIs               |
|   3 | Backend Architecture    |
|   4 | Web Authentication      |
|   5 | Databases & ORM         |
|   6 | Web Security            |
|   7 | Web Performance         |
|   8 | Testing & Debugging     |
|   9 | Background Processing   |
|  10 | Web Deployment          |
|  11 | Software Architecture   |
|  12 | Python Web Ecosystem    |

### 📖 Term Details

Every glossary term provides:

- Term name
- Category
- Learning level
- Definition
- Example
- Related terms
- Previous term
- Next term

### 🌐 Project Versions

The Flask version includes a dedicated **Versions** page connecting the different Tech Glossary Hub implementations.

| Version | Technology              | Status          |
| ------- | ----------------------- | --------------- |
| Flask   | Flask                   | Current Version |
| Django  | Django                  | Available       |
| HTML    | HTML / CSS / JavaScript | Available       |
| React   | React + Vite            | Available       |
| Angular | Angular                 | Available       |

### 📱 Responsive Design

The interface is designed to work across:

- Desktop
- Laptop
- Tablet
- Mobile devices

### ♿ Accessibility Foundation

The project includes basic accessibility improvements such as:

- Skip-to-content link
- Visible keyboard focus states
- `:focus-visible` support
- Visually hidden utility class
- Reduced-motion support
- Semantic page structure

### 🌙 Developer-Oriented Dark UI

The application uses a dark developer-focused interface featuring:

- Dark background
- Surface-based cards
- Cyan/blue accent color
- Responsive layouts
- Subtle borders
- Hover interactions
- Developer-style typography

---

## 🛠️ Technology Stack

### Backend

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **Jinja2**

### Database

- **SQLite**
- **SQLAlchemy ORM**

### Frontend

- **HTML5**
- **CSS3**
- **JavaScript**
- **Jinja Templates**

### Development Tools

- Git
- GitHub
- Visual Studio Code
- Python Virtual Environment

### Deployment

- Vercel

---

## 📂 Project Structure

```text
tech-glossary-hub-flask/
│
├── app/
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── category.py
│   │   └── glossary_term.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── categories.html
│   │   ├── category_detail.html
│   │   ├── glossary.html
│   │   ├── term_detail.html
│   │   ├── versions.html
│   │   ├── contact.html
│   │   ├── about.html
│   │   │
│   │   └── components/
│   │       ├── navbar.html
│   │       └── footer.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── components.css
│   │   │
│   │   └── js/
│   │       └── main.js
│   │
│   └── __init__.py
│
├── instance/
│   └── glossary.db
│
├── config.py
├── run.py
├── seed.py
├── check_database.py
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Structure

The application uses **SQLite through Flask-SQLAlchemy**.

### Category

The `Category` model stores:

- Category ID
- Category name
- Category slug
- Category description
- Related glossary terms

### GlossaryTerm

The `GlossaryTerm` model stores:

- Term ID
- Term name
- Term slug
- Definition
- Example
- Learning level
- Category relationship
- Creation timestamp

### Database Relationship

```text
Category
    │
    │ 1
    │
    ├───────────────┐
    │               │
    │ *             │
    ▼               ▼
GlossaryTerm    GlossaryTerm
```

A category can contain multiple glossary terms.

---

## 📊 Glossary Dataset

The current dataset contains:

```text
Total Categories: 12
Total Terms:      250
```

### Learning Levels

```text
Beginner
Moderate
Advanced
```

The terms are distributed across the 12 Flask-focused technical categories.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/charanepuri/tech-glossary-hub-flask.git
```

### 2. Navigate to the Project

```bash
cd tech-glossary-hub-flask
```

### 3. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Initialize / Seed the Database

```bash
python seed.py
```

The seed script creates the categories and glossary terms.

### 7. Check the Database

```bash
python check_database.py
```

This displays:

- Total categories
- Total glossary terms
- Category-wise term counts
- Learning-level counts

### 8. Start the Flask Application

```bash
python run.py
```

The application will start on the local Flask development server.

Open the local address shown in the terminal.

---

## 🔗 Main Routes

| Route              | Purpose                        |
| ------------------ | ------------------------------ |
| `/`                | Home page                      |
| `/categories`      | All categories                 |
| `/category/<slug>` | Category details               |
| `/glossary`        | Glossary search and pagination |
| `/term/<slug>`     | Individual term                |
| `/versions`        | Project versions               |
| `/contact`         | Contact information            |
| `/about`           | Project information            |

---

## 🔍 Glossary Search

The glossary supports query-based searching.

### Search by Term

```text
/glossary?q=flask
```

### Filter by Category

```text
/glossary?category=rest-apis
```

### Combined Search and Category Filtering

```text
/glossary?q=api&category=rest-apis
```

This allows users to narrow glossary results using both search queries and category filters.

---

## 🎨 Design System

The application uses a dark, developer-oriented design system.

### Primary Colors

```css
--background: #0b1120;
--surface: #111827;
--surface-light: #172033;

--primary: #38bdf8;
--primary-dark: #0284c7;

--text: #f8fafc;
--text-secondary: #cbd5e1;
--muted: #94a3b8;
```

### UI Characteristics

- Rounded cards
- Subtle borders
- Cyan highlights
- Responsive grids
- Hover animations
- Accessible focus indicators
- Developer-focused typography

---

## 🧩 Application Architecture

The application follows a modular Flask structure.

### 🏭 Application Factory

The Flask application is initialized through the **Application Factory Pattern**.

### 🔀 Blueprints

Application routes are organized using Flask Blueprints.

The main blueprint handles:

```text
Home
Categories
Category Details
Glossary
Term Details
Versions
Contact
About
```

### 🗄️ Models

Database models are separated from routes and application configuration.

```text
app/
└── models/
    ├── category.py
    └── glossary_term.py
```

### 📄 Templates

Jinja templates are organized into:

```text
Base Template
Page Templates
Reusable Components
```

Reusable components include:

```text
Navbar
Footer
```

### 🎨 Static Files

Frontend assets are separated into:

```text
CSS
JavaScript
```

---

## 🔐 Security Considerations

This project is primarily an educational Flask application.

Recommended production improvements include:

- Environment variables for secrets
- CSRF protection for forms
- Production WSGI server
- Secure session configuration
- HTTPS
- Secure cookies
- Database migration management
- Input validation
- Rate limiting where appropriate

---

## 🧪 Testing & Verification

Before committing changes, verify the following.

### Application

```bash
python run.py
```

### Database

```bash
python check_database.py
```

### Build / Syntax

```bash
python -m compileall .
```

### Browser Verification

Check:

- Homepage
- Categories
- Category details
- Glossary
- Search
- Category filtering
- Pagination
- Term details
- Related terms
- Versions
- Contact
- About
- Responsive layout
- Keyboard navigation

---

## ♿ Accessibility

The project includes an accessibility foundation with:

- Skip navigation link
- Keyboard focus indicators
- Semantic `<main>` element
- Visually hidden utility class
- Reduced-motion media query
- Keyboard-friendly interactive elements

The accessibility work provides a foundation for future UX improvements.

---

## 🌐 Other Tech Glossary Hub Versions

Tech Glossary Hub is being developed across multiple technologies.

### 🔥 Flask Version

**GitHub:**
https://github.com/charanepuri/tech-glossary-hub-flask

**Live:**
https://tech-glossary-hub-flask.onrender.com/

### 🐍 Django Version

**GitHub:**
https://github.com/charanepuri/tech-glossary-hub

**Live:**
https://tech-glossary-hub.onrender.com/

### 🌐 HTML Version

**GitHub:**
https://github.com/charanepuri/tech-glossary-hub-html

**Live:**
https://charanepuri.github.io/tech-glossary-hub-html/

### ⚛️ React Version

**GitHub:**
https://github.com/charanepuri/tech-glossary-hub-react

**Live:**
https://tech-glossary-hub-react.vercel.app/

### 🅰️ Angular Version

**GitHub:**
https://github.com/charanepuri/tech-glossary-hub-angular

**Live:**
https://tech-glossary-hub-angular.vercel.app/home

---

## 📌 Project Links

| Resource       | Link                                                     |
| -------------- | -------------------------------------------------------- |
| Flask GitHub   | https://github.com/charanepuri/tech-glossary-hub-flask   |
| Flask Live     | https://tech-glossary-hub-flask.onrender.com/            |
| Django GitHub  | https://github.com/charanepuri/tech-glossary-hub         |
| Django Live    | https://tech-glossary-hub.onrender.com/                  |
| HTML GitHub    | https://github.com/charanepuri/tech-glossary-hub-html    |
| HTML Live      | https://charanepuri.github.io/tech-glossary-hub-html/    |
| React GitHub   | https://github.com/charanepuri/tech-glossary-hub-react   |
| React Live     | https://tech-glossary-hub-react.vercel.app/              |
| Angular GitHub | https://github.com/charanepuri/tech-glossary-hub-angular |
| Angular Live   | https://tech-glossary-hub-angular.vercel.app/home        |

---

## 👨‍💻 Developer

### Epuri Charan Teja

**Aspiring Python Full Stack Developer**

### 🔗 GitHub

https://github.com/charanepuri

### 💼 LinkedIn

https://www.linkedin.com/in/charan-teja-972aa9231

### 🌐 Flask Portfolio

https://flask-developer-dashboard-portfolio.onrender.com/

### 📧 Email

[Charanepuri26@gmail.com](mailto:Charanepuri26@gmail.com)

---

## 📌 Project Status

**Current Version:** Flask Edition

**Status:** Development / Learning Project

The project is being developed incrementally with a focus on:

- Flask fundamentals
- Backend architecture
- Database integration
- Jinja templating
- Search and filtering
- Responsive frontend development
- Accessibility
- Clean project organization
- Deployment readiness

---

## 📄 License

This project is created for **educational, portfolio, and learning purposes**.

---

## ⭐ Acknowledgment

This project is part of a broader learning journey focused on building practical web applications using **Python and modern web technologies**.

---

<div align="center">

### 📚 Tech Glossary Hub — Flask

**Learn · Explore · Build**

Built with **Flask · SQLAlchemy · SQLite · HTML · CSS · JavaScript**

</div>
