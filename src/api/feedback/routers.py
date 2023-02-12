from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from .resources import Feedback


blueprint = Blueprint("feedback", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(Feedback, "/feedbacks", endpoint="feedbacks")

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
