from flask import Flask

from config import Config
from app.extensions import db, bcrypt, migrate, login_manager
from app.models.user import User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = '/'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    migrate.init_app(app, db)
    # Register blueprints here
    from app.home import bp as landing
    app.register_blueprint(landing)

    from app.company_registration import bp as company_registration
    app.register_blueprint(company_registration, url_prefix='/company_registration')

    from app.login import bp as login
    app.register_blueprint(login, url_prefix='/login')

    from app.dashboard import bp as dashboard
    app.register_blueprint(dashboard, url_prefix='/dashboard')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
