from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """
    This is the class which we will use to create the users for the app
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    profile_pic  = db.Column(db.String)
    pitches = db.relationship("Pitch", backref= "user", lazy="dynamic")
    comments = db.relationship("Comment", backref="user", lazy="dynamic")
    pass_locked = db.relationship(db.String)

    @property
    def password(self):
        raise AttributeError("Gerrarahia")

    @password.setter
    def password(self,password):
        self.pass_locked = generate_password_hash(password)

    def verify_pass(self,password):
        return check_password_hash(self.pass_locked,password)

    def get_user_pitches(self):
        user = User.query.filter_by(id = self.id).first()
        return user.pitches

class Pitch(db.Model):
    """
    This is the class which we will use to create the pitches for the app
    """
    __tablename__ = "pitches"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref = "pitch", lazy = "dynamic")

    def save_pitch(self):
        db.session(self)
        db.session.commit()

    def get_pitch_comments(self):
        pitch = Pitch.query.filter_by(id = self.id).first()
        return pitch.comments

class Comment(db.Model):
    """
    This is the class which we will use to create the comments for the pitches
    """

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
