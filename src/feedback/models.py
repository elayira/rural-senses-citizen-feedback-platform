from flask_mongoengine import Document
import mongoengine as me
from src.user.models import User

MESSAGE_STATUS = (
    'sent',
    'read'
)


class Community(me.EmbeddedDocument):
    size = me.IntField(required=True)
    name = me.StringField(required=True)


class Issue(me.EmbeddedDocument):
    concern = me.StringField(required=True)
    age = me.IntField(required=True)


class Feedback(Document):
    """Community feedback model"""
    community = me.DictField(me.EmbeddedDocumentField(Community))
    issues = me.EmbeddedDocumentListField(Issue)
    submitted_by = me.ReferenceField(User)
    submitted_on = me.DateField()


class Message(Document):
    community = me.DictField(me.EmbeddedDocumentField(Community))
    sender = me.ReferenceField(User)
    recipient = me.ReferenceField(User)
    content = me.StringField()
    status = me.StringField(choices=MESSAGE_STATUS)
