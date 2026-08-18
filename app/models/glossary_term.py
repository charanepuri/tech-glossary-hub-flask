from datetime import datetime, timezone

from app import db


class GlossaryTerm(db.Model):
    __tablename__ = "glossary_terms"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    slug = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    definition = db.Column(
        db.Text,
        nullable=False
    )

    example = db.Column(
        db.Text,
        nullable=True
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    category = db.relationship(
        "Category",
        back_populates="terms"
    )

    def __repr__(self):
        return f"<GlossaryTerm {self.name}>"