from src.extensions import pwd_context
from flask_mongoengine import Document
import mongoengine as me


class User(Document):
    """Basic user model"""

    username = me.StringField(required=True, unique=True)
    password = me.StringField(max_length=255, required=True)
    active = me.BooleanField(default=True)
