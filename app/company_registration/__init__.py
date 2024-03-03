from flask import Blueprint

bp = Blueprint('company_registration', __name__)

from app.company_registration import routes
