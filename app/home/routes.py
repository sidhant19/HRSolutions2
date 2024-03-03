from app.home import bp
from flask import render_template, request, redirect, url_for
from app.models.company import Company


@bp.route('/', methods=['GET', 'POST'])
def landing_page():

    if request.method == 'POST':
        if not Company.query.filter_by(company_code=request.form['companyCode']).first():
            return render_template('home.html', error=1)

        return redirect(url_for('login.login', code=request.form['companyCode']))
    return render_template('home.html', error=0)
