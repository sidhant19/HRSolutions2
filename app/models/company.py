from app.extensions import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.Text)
    company_code = db.Column(db.Integer)
    company_identification_number = db.Column(db.Text)

