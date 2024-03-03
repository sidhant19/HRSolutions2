from app.extensions import db


class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, nullable=False)
    receiver = db.Column(db.Integer, nullable=False)
    request_tag = db.Column(db.Text)
    info = db.Column(db.Text)
    approval = db.Column(db.Boolean)
    comments = db.Column(db.Text)
