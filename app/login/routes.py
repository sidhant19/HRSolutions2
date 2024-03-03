from app.login import bp
from datetime import datetime
from flask import render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from app.extensions import bcrypt, db
from flask_login import login_user, login_required, current_user, logout_user
from sqlalchemy import and_
from app.models.user import User
import json


class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


def log_write(log):
    fn = "logs.json"
    with open(fn, 'r') as f:
        fd = json.load(f)
    fd.append(log)
    with open(fn, 'w') as f:
        json.dump(fd, f)


@bp.route('/<int:code>', methods=['GET', 'POST'])
def login(code):
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(and_(User.username == form.username.data, User.company_code == code)).first()

        if user:
            if not user.last_login:

                login_user(user)
                user.last_login = datetime.now()
                db.session.commit()
                return redirect(url_for("login.new_password"))

            elif bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                user.last_login = datetime.now()
                db.session.commit()
                log_write({"user": f"{form.username.data}",
                           "tag": "login", "detail": "User Logged In", "time": f"{user.last_login}"})
                return redirect(url_for('dashboard.dashboard'))
        user = User.query.filter_by(email=form.username.data).first()

        if user:
            if not user.last_login:
                login_user(user)
                user.last_login = datetime.now()
                db.session.commit()
                return redirect(url_for("login.new_password"))

            elif bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                user.last_login = datetime.now()
                db.session.commit()
                log_write({"user": f"{form.username.data}",
                           "tag": "login", "detail": "User Logged In", "time": f"{user.last_login}"})
                return redirect(url_for('dashboard.dashboard'))
    return render_template('login.html', form=form, code=code)


@bp.route('/new_password', methods=['GET', 'POST'])
@login_required
def new_password():
    print(3)
    if request.method == 'POST':
        new_pass = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_pass == confirm_password:
            hashed_password = bcrypt.generate_password_hash(new_pass)
            u = User.query.filter_by(id=current_user.id).first()
            u.password = hashed_password
            db.session.commit()
            return redirect(url_for('login.login', code=current_user.company_code))
        else:
            # Passwords don't match, handle accordingly (e.g., show an error message)
            pass

    return render_template('new_password.html')


@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    log_write({
        "user": f"{current_user.username}", "tag": "logout", "detail": "User Logged Out", "time": f"{datetime.now()}"})
    logout_user()
    return redirect(url_for('home.landing_page'))
