from app.extensions import db
from flask_login import UserMixin
from sqlalchemy import UniqueConstraint


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date)
    level = db.Column(db.Integer, nullable=False)
    last_login = db.Column(db.DateTime)
    attendance = db.Column(db.Text)
    designation = db.Column(db.Text)
    address = db.Column(db.Text)
    address_proof = db.Column(db.Text)
    identity_proof = db.Column(db.Text)
    other_documents = db.Column(db.Text)
    basic_salary = db.Column(db.Integer)
    dearance_allowance = db.Column(db.Integer)
    house_rent_allowance = db.Column(db.Integer)
    conveyance_allowance = db.Column(db.Integer)
    manager = db.Column(db.Integer)
    company_code = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('username', 'company_code', name='primary_comapany_username'),
    )
