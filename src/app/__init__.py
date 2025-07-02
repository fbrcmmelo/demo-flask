from flask import Flask
from app.core.models.user_entity import db
from app.core.configs.db_config import DBConfig
from app.routes.users.users_routes import users_bp

def create_app() -> Flask:
    """
    Create and configure the Flask application.
    Returns:
        Flask app instance.
    """
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(DBConfig)
    db.init_app(app)
   
    with app.app_context():
        db.create_all()

    app.register_blueprint(users_bp)
    return app
