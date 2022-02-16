import sqlalchemy
from settings import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_login import LoginManager, login_manager, UserMixin, current_user

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

_metadata = MetaData(naming_convention=convention)

# Database connect
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lidosta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, metadata=_metadata)

# Migrations
migrate = Migrate(app, db, render_As_batch=True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nosuakums = db.Column(db.String(300), nullable=False)
    bilde = db.Column(db.Text, unique=True)
    name = db.Column(db.String(300), nullable=False)
    children = db.relationship("Arsti", cascade="all, delete")

    def __repr__(self):
        return '<Item %r>' % self.id