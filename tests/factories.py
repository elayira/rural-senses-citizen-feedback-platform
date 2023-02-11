import factory
from src.models import User


class UserFactory(factory.Factory):

    username = factory.Sequence(lambda n: "user%d" % n)
    username = factory.Sequence(lambda n: "user%d@mail.com" % n)
    password = "mypwd"

    class Meta:
        model = User
