from django.db.models import Model,UUIDField,CharField,IntegerField,DateTimeField
from uuid import uuid4
class Languages(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    name = CharField(max_length=200,primary_key=False,null=False,unique=True,editable=False)
    code = IntegerField(primary_key=False,null=False,unique=True,editable=False)
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=True,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=True,editable=False)
