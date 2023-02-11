from flask import Flask
from src import manage
from flask_mongoengine import MongoEngine
from src.extensions import apispec
from src.extensions import jwt
from src.config import MONGODB_SETTINGS

def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("citizen_feedback")
    app.config.from_object("src.config")
    app.config["MONGODB_SETTINGS"] = MONGODB_SETTINGS
    MongoEngine().init_app(app)

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)
    configure_cli(app)
    configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """Configure flask extensions"""
    jwt.init_app(app)


def configure_cli(app):
    """Configure Flask 2.0's cli for easy entity management"""
    app.cli.add_command(manage.createSuperAdmin)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """Register all blueprints for application"""
    from src.api.auth import blueprint as auth_blueprint
    from src.api.user import routers as user_router
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_router.blueprint)
