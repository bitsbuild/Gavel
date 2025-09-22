from django.db.models import (
    Model,
    UUIDField,
    CharField,
    IntegerField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    UniqueConstraint)
from django.contrib.auth.models import User
from uuid import uuid4
class Language(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    name = CharField(max_length=200,primary_key=False,null=False,unique=True,editable=True)
    code = IntegerField(primary_key=False,null=False,unique=True,editable=True)
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=False,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=False,editable=False)
    def __str__(self):
        return self.name
class ProblemSet(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    name = CharField(primary_key=False,null=False,unique=True,editable=True)
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=False,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=False,editable=False)
    def __str__(self):
        return self.name
class Problem(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    name = CharField(max_length=200,primary_key=False,null=False,unique=True,editable=True)
    description = CharField(primary_key=False,null=False,unique=False,editable=True)
    constraints = CharField(primary_key=False,null=False,unique=False,editable=True)
    examples = CharField(primary_key=False,null=False,unique=False,editable=True)
    problem_input = CharField(primary_key=False,null=False,unique=False,editable=True)
    problem_expected_output = CharField(primary_key=False,null=False,unique=False,editable=True)
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=False,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=False,editable=False)
    def __str__(self):
        return self.name
class ProblemSetMapping(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    problem = ForeignKey(Problem,on_delete=CASCADE,related_name='mapping')
    problem_set = ForeignKey(ProblemSet,on_delete=CASCADE,related_name='mapping')
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=False,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=False,editable=False)
    def __str__(self):
        return str(self.id)  
class Status(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    name = CharField(max_length=200,primary_key=False,null=False,unique=True,editable=True)
    code = IntegerField(primary_key=False,null=False,unique=True,editable=True)
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=False,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=False,editable=False)
    def __str__(self):
        return self.name
class Submission(Model):
    id = UUIDField(default=uuid4,primary_key=True,null=False,unique=True,editable=False)
    user = ForeignKey(User,on_delete=CASCADE,related_name='submissions')
    problem = ForeignKey(Problem,on_delete=CASCADE,related_name='submissions')
    status = ForeignKey(Status,on_delete=CASCADE,related_name='submissions')
    submitted_solution = CharField(primary_key=False,null=False,unique=False,editable=True)
    created = DateTimeField(auto_now_add=True,primary_key=False,null=False,unique=False,editable=False)
    updated = DateTimeField(auto_now=True,primary_key=False,null=False,unique=False,editable=False)
    def __str__(self):
        return str(self.id) 