from app.dashboard import bp
from flask import render_template
from flask_login import login_required


@bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('base.html')
