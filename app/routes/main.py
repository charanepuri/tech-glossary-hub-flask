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