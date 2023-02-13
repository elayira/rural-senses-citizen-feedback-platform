import os
from flask import Flask
from src import manage
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from src.extensions import apispec, jwt, rbac
from src import config

def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("citizen_feedback")
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, config.UPLOAD_FOLDER)
    app.config['MAX_CONTENT_LENGTH'] = 12 * 1024 * 1024
    app.config.from_object("src.config")
    app.config["MONGODB_SETTINGS"] = config.MONGODB_SETTINGS
    app.config['RBAC_USE_WHITE'] = True
    rbac.init_app(app)
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
    from src.api.feedback import routers as feedback_router
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_router.blueprint)
    app.register_blueprint(feedback_router.blueprint)
