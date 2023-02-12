from marshmallow_mongoengine import ModelSchema
from .models import Feedback


class FeedbackSchema(ModelSchema):
    class Meta:
        model = Feedback
        load_instance = True
