from app.company_registration import bp
from flask import render_template, request, redirect, url_for
import random
from app.models.company import Company
from app.models.user import User
from app.extensions import db, bcrypt
from datetime import datetime


def generate_company_code():
    while True:
        code = random.randint(100000, 999999)
        if not Company.query.filter_by(company_code=code).first():
            return code


@bp.route('/', methods=['GET', 'POST'])
def company_registration():
    if request.method == 'POST':
        if Company.query.filter_by(company_identification_number=request.form['companyID']).first():
            return redirect(url_for("company_registration.company_registration"))
        company_code_generated = generate_company_code()
        company_info = Company(company_identification_number=request.form['companyID'],
                               company_name=request.form['companyName'],
                               company_code=company_code_generated)
        admin_info = User(name=request.form['adminName'],
                          email=request.form['email'],
                          phone=request.form['phone'],
                          dob=datetime.strptime(request.form['dob'], '%Y-%m-%d').date(),
                          username="admin",
                          level=0,
                          last_login=None,
                          company_code=company_code_generated,
                          password=bcrypt.generate_password_hash(request.form['password']))

        db.session.add(company_info)
        db.session.add(admin_info)
        db.session.commit()
        return redirect(url_for('company_registration.company_code', code=company_code_generated))
    return render_template('company_registration/company_registration.html')


@bp.route('/company_code/<code>')
def company_code(code):
    return render_template('company_registration/company_code.html', code=code)
