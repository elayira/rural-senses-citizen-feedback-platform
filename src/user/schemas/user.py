from marshmallow_mongoengine import ModelSchema
from src.user.models import User
from src.extensions import ma


class UserSchema(ModelSchema):
    password = ma.String(load_only=True, required=True)

    class Meta:
        model = User
        load_instance = True
