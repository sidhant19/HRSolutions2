from app.extensions import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, nullable=False)
    receiver = db.Column(db.Integer, nullable=False)
    msg_type = db.Column(db.Text)
    msg = db.Column(db.Text)
    read = db.Column(db.Boolean, default=False)
    send_time = db.Column(db.DateTime)
    read_time = db.Column(db.DateTime)
