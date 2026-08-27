from flask import Blueprint, render_template

from app.models import Category, GlossaryTerm


main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
def home():
    categories = Category.query.order_by(Category.name.asc()).all()

    total_categories = Category.query.count()
    total_terms = GlossaryTerm.query.count()

    return render_template(
        "home.html",
        categories=categories,
        total_categories=total_categories,
        total_terms=total_terms
    )


@main_bp.route("/categories")
def categories():
    categories = Category.query.order_by(Category.name.asc()).all()

    return render_template(
        "categories.html",
        categories=categories
    )


@main_bp.route("/category/<slug>")
def category_detail(slug):
    category = Category.query.filter_by(
        slug=slug
    ).first_or_404()

    terms = GlossaryTerm.query.filter_by(
        category_id=category.id
    ).order_by(
        GlossaryTerm.name.asc()
    ).all()

    return render_template(
        "category_detail.html",
        category=category,
        terms=terms
    )