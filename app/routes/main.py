from flask import Blueprint, render_template, request
from sqlalchemy import or_

from app.models import Category, GlossaryTerm


# ============================================
# MAIN BLUEPRINT
# ============================================

main_bp = Blueprint(
    "main",
    __name__
)


# ============================================
# HOME
# ============================================

@main_bp.route("/")
def home():

    categories = Category.query.order_by(
        Category.name.asc()
    ).all()

    total_categories = Category.query.count()

    total_terms = GlossaryTerm.query.count()

    return render_template(
        "home.html",
        categories=categories,
        total_categories=total_categories,
        total_terms=total_terms
    )


# ============================================
# CATEGORIES
# ============================================

@main_bp.route("/categories")
def categories():

    categories = Category.query.order_by(
        Category.name.asc()
    ).all()

    return render_template(
        "categories.html",
        categories=categories
    )


# ============================================
# CATEGORY DETAIL
# ============================================

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


# ============================================
# GLOSSARY
# ============================================

@main_bp.route("/glossary")
def glossary():

    # ----------------------------------------
    # Search Query
    # ----------------------------------------

    search_query = request.args.get(
        "q",
        ""
    ).strip()


    # ----------------------------------------
    # Category Filter
    # ----------------------------------------

    category_slug = request.args.get(
        "category",
        ""
    ).strip()


    # ----------------------------------------
    # Pagination
    # ----------------------------------------

    page = request.args.get(
        "page",
        1,
        type=int
    )

    if page < 1:
        page = 1


    # ----------------------------------------
    # Categories
    # ----------------------------------------

    categories = Category.query.order_by(
        Category.name.asc()
    ).all()


    # ----------------------------------------
    # Base Query
    # ----------------------------------------

    query = GlossaryTerm.query


    # ----------------------------------------
    # Search Filter
    # ----------------------------------------

    if search_query:

        search_pattern = f"%{search_query}%"

        query = query.filter(
            or_(
                GlossaryTerm.name.ilike(
                    search_pattern
                ),

                GlossaryTerm.definition.ilike(
                    search_pattern
                ),

                GlossaryTerm.example.ilike(
                    search_pattern
                )
            )
        )


    # ----------------------------------------
    # Category Filter
    # ----------------------------------------

    if category_slug:

        query = query.join(
            GlossaryTerm.category
        ).filter(
            Category.slug == category_slug
        )


    # ----------------------------------------
    # Pagination
    # ----------------------------------------

    pagination = query.order_by(
        GlossaryTerm.name.asc()
    ).paginate(
        page=page,
        per_page=6,
        error_out=False
    )


    # ----------------------------------------
    # Selected Category
    # ----------------------------------------

    selected_category = None

    if category_slug:

        selected_category = Category.query.filter_by(
            slug=category_slug
        ).first()


    # ----------------------------------------
    # Render Glossary
    # ----------------------------------------

    return render_template(
        "glossary.html",
        terms=pagination.items,
        pagination=pagination,
        categories=categories,
        search_query=search_query,
        category_slug=category_slug,
        selected_category=selected_category
    )


# ============================================
# TERM DETAIL
# ============================================

@main_bp.route("/term/<slug>")
def term_detail(slug):

    # ----------------------------------------
    # Get Current Term
    # ----------------------------------------

    term = GlossaryTerm.query.filter_by(
        slug=slug
    ).first_or_404()


    # ----------------------------------------
    # Get Terms From Same Category
    # ----------------------------------------

    category_terms = GlossaryTerm.query.filter_by(
        category_id=term.category_id
    ).order_by(
        GlossaryTerm.name.asc()
    ).all()


    # ----------------------------------------
    # Find Current Term Position
    # ----------------------------------------

    current_index = next(
        (
            index
            for index, item in enumerate(
                category_terms
            )
            if item.id == term.id
        ),
        None
    )


    # ----------------------------------------
    # Previous / Next Terms
    # ----------------------------------------

    previous_term = None

    next_term = None


    if current_index is not None:

        if current_index > 0:

            previous_term = category_terms[
                current_index - 1
            ]


        if current_index < len(category_terms) - 1:

            next_term = category_terms[
                current_index + 1
            ]


    # ----------------------------------------
    # Related Terms
    # ----------------------------------------

    related_terms = GlossaryTerm.query.filter(
        GlossaryTerm.category_id == term.category_id,
        GlossaryTerm.id != term.id
    ).order_by(
        GlossaryTerm.name.asc()
    ).limit(4).all()


    # ----------------------------------------
    # Render Term Detail
    # ----------------------------------------

    return render_template(
        "term_detail.html",
        term=term,
        related_terms=related_terms,
        previous_term=previous_term,
        next_term=next_term
    )