from __future__ import annotations
import logging
from mongoengine.errors import DoesNotExist
from src.commons.pagination import paginate
from src.user.schemas.user import UserSchema
from src.user.models import User
from src.extensions import pwd_context


logger = logging.getLogger(__name__)


class UserService:
    model = User
    schema = UserSchema
    
    def user(self, **field):
        """Retrieve user data"""
        try:
            return self.model.objects.get(**field)
        except DoesNotExist:
            logger.info("Invalid user ID: {pk}")
    
    def users(self):
        return paginate(self.model.objects, self.schema(many=True))
    
    def createuser(self, **fields):
        if fields.get('password', None):
            fields['password'] = pwd_context.hash(fields['password'])
        user = self.schema().load(fields)
        user.save()
        return user

    def updateuser(self, pk, fields):
        try:
            user = self.model.objects.get(id=pk)
            user = self.schema(partial=True).load(fields, instance=user)
            user.save()
            return user
        except DoesNotExist:
            logger.info("Invalid user ID: {pk}")
    
    def deleteuser(self, pk):
        try:
            user = self.model.objects.get(id=pk)
            user.delete()
            return pk
        except DoesNotExist:
            logger.info("Invalid user ID: {pk}")
