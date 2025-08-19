from django.db.models import Model,UUIDField,CharField,DateTimeField
from uuid import uuid4
class Language(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    name = CharField(null=False,editable=True,primary_key=False)
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)
class Set(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    name = CharField(null=False,editable=True,primary_key=False)
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)    
class Challenge(Model):
    pass
class TestCase(Model):
    pass
class Submission(Model):
    pass
class UserRecord(Model):
    pass