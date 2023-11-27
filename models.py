from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models ##############################

DEFAULT_IMAGE = "https://cdn2.vectorstock.com/i/1000x1000/17/61/dog-icon-on-white-circle-with-a-long-shadow-vector-20151761.jpg"

class Pet(db.Model):

    """Pets that are for adoption"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=False)
    species = db.Column(db.Text, nullable=False, unique=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=True, default=True)

    def image_url(self):
        """Return image for pets"""
        return self.photo_url or DEFAULT_IMAGE
