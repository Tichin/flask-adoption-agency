"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

PHOTO_URL = 'https://en.wikipedia.org/wiki/Van_cat#/media/File:VAN_CAT.png'

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Pet """

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(50),
        nullable=False
    )

    # species = db.Column(
    #     db.String(20),
    #     nullable=False,
    #     CheckConstraint=(['cat', 'dog', 'porcupine'])
    # )

    species = db.Column(
        db.String(20),
        nullable=False
    )

    photo_url = db.Column(
        db.String(),
        nullable=False,
        default='https://clipartix.com/wp-content/uploads/2016/10/Lion-paw-print-clipart-kid.png'
    )

    # age = db.Column(
    #     db.String(),
    #     nullable=False,
    #     CheckConstraint=(['baby', 'young', 'adult', 'senior'])
    # )

    age = db.Column(
        db.String(),
        nullable=False
    )

    note = db.Column(
        db.String()
    )

    available = db.Column(
        db.Boolean(),
        nullable=False,
        default=True
    )
