"""Simple blocklist implementation using database

Using database may not be your prefered solution to handle blocklist in your
final application, but remember that's just a cookiecutter template. Feel free
to dump this code and adapt it for your needs.

For this reason, we don't include advanced tokens management in this
example (view all tokens for a user, revoke from api, etc.)

If we choose to use database to handle blocklist in this example, it's mainly
because it will allow you to run the example without needing to setup anything else
like a redis or a memcached server.

This example is heavily inspired by
https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/blocklist_database.py
"""
from flask_mongoengine import Document
import mongoengine as me
from src.user.models import User

class TokenBlocklist(Document):
    """Blocklist representation"""

    jti = me.StringField(required=True, max_length=36)
    token_type = me.StringField(required=True, max_length=10)
    user_id = me.ReferenceField(User)
    revoked = me.BooleanField()
    expires = me.DateTimeField()

    def to_dict(self):
        return {
            "jti": self.jti,
            "token_type": self.token_type,
            "user_identity": self.user_identity,
            "revoked": self.revoked,
            "expires": self.expires,
        }
