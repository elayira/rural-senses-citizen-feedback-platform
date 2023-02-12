from flask_mongoengine import Document
from enum import Enum
import mongoengine as me
from src.user.models import User

MESSAGE_STATUS = [
    ('SE', 'SENT'),
    ('RE', 'READ')
]

class IssueType(str, Enum):
    FAMILY = 'FAMILY'
    HEALTH = 'HEALTH'
    UNKNOWN = 'UNKNOWN'

    @classmethod
    def values(cls):
        return [member.value for member in cls]


class IssueAnalysis(me.EmbeddedDocument):
    family_concern_freq_ratio = me.FloatField()
    health_concern_freq_ratio = me.FloatField()
    unknown_concern_freq_ratio = me.FloatField()


class Community(me.EmbeddedDocument):
    size = me.IntField(required=True)
    name = me.StringField(required=True)


class Issue(me.EmbeddedDocument):
    concern = me.StringField(required=True)
    age = me.IntField(required=True)
    classification = me.StringField(choices=IssueType.values())


class Feedback(Document):
    """Community feedback model"""
    created_at = me.FloatField()
    community = me.EmbeddedDocumentField(Community)
    issues = me.ListField(me.EmbeddedDocumentField(Issue))
    submitted_by = me.ReferenceField(User)
    csv_path = me.StringField()
    issue_analysis = me.EmbeddedDocumentField(IssueAnalysis)


class Message(Document):
    community = me.DictField(me.EmbeddedDocumentField(Community))
    sender = me.ReferenceField(User)
    recipient = me.ReferenceField(User)
    content = me.StringField()
    status = me.StringField(choices=MESSAGE_STATUS, default='se')
