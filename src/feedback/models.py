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
    created_at = me.FloatField()
    community = me.EmbeddedDocumentField(Community)
    issues = me.ListField(me.EmbeddedDocumentField(Issue))
    submitted_by = me.ReferenceField(User)
    csv_path = me.StringField()


class Message(Document):
    community = me.DictField(me.EmbeddedDocumentField(Community))
    sender = me.ReferenceField(User)
    recipient = me.ReferenceField(User)
    content = me.StringField()
    status = me.StringField(choices=MESSAGE_STATUS)
