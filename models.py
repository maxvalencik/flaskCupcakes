"""Models for flask cupcakes"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.
    To be call in app file
    """

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake table"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    image = db.Column(db.Text, default="https://tinyurl.com/demo-cupcake")

    def to_dict(self):
        """Serialize cupcake to a dictionary of cupcake info."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }
