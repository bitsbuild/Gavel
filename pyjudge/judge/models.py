from django.db.models import (Model,
                              UUIDField,
                              CharField,
                              DateTimeField,
                              TextField,
                              ForeignKey,
                              CASCADE,
                              UniqueConstraint,
                              FileField,
                              BooleanField,
                              IntegerField,
                              ManyToManyField)
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from uuid import uuid4
import os
def validate_file_type(value):
    file_ext = os.path.splitext(value.name)[1]
    if file_ext.lower() not in ['.py','.cpp','.js','.java']:
        raise ValidationError("Language Not Supported")
def path_for_testcase(instance,filename):
    file_ext = os.path.splitext(filename)[1]
    return f"{instance.challenge.name}/{instance.language.name}{file_ext}"
def path_for_solution(instance,filename):
    file_ext = os.path.splitext(filename)[1]
    return f"{instance.challenge.name}/{instance.user.username}/{instance.language.name}{file_ext}"
class Language(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    name = CharField(null=False,editable=True,primary_key=False)
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)
    def __str__(self):
        return self.name
class Set(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    name = CharField(null=False,editable=True,primary_key=False)
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)
    def __str__(self):
        return self.name    
class Challenge(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    name = CharField(null=False,editable=True,primary_key=False)
    challenge_body = TextField(null=False,editable=True,primary_key=False)
    constraints = TextField(null=False,editable=True,primary_key=False)
    input_instruction = TextField(null=False,editable=True,primary_key=False)
    output_instruction = TextField(null=False,editable=True,primary_key=False)
    code_format = TextField(null=False,editable=True,primary_key=False)
    challenge_set = ManyToManyField(Set,related_name="questions")
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)
    def __str__(self):
        return self.name
class TestCase(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    language = ForeignKey(Language,related_name="test_case",on_delete=CASCADE)
    challenge = ForeignKey(Challenge,related_name="test_case",on_delete=CASCADE)
    test_case = FileField(upload_to=path_for_testcase,validators=[validate_file_type])
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)
    class Meta:
        constraints = [
            UniqueConstraint(fields=['language','challenge'],name='one-test-case-per-language-per-challenge')
        ]
    def __str__(self):
        return f"{self.challenge.name}-{self.language.name}"
class Submission(Model):
    id = UUIDField(default=uuid4,null=False,editable=False,primary_key=True)
    user = ForeignKey(User,related_name='submissions',on_delete=CASCADE)
    challenge = ForeignKey(Challenge,related_name="solution",on_delete=CASCADE)
    language = ForeignKey(Language,related_name="solution",on_delete=CASCADE)
    solution_file = FileField(upload_to=path_for_solution)
    outcome = BooleanField(default=False,editable=False,null=False,primary_key=False)
    number_of_test_cases = IntegerField(default=0,editable=False,null=False,primary_key=False)
    created = DateTimeField(auto_now_add=True,null=False,editable=False,primary_key=False)
    updated = DateTimeField(auto_now=True,null=False,editable=False,primary_key=False)
    def __str__(self):
        return f"{self.user.username}-{self.challenge.name}-{self.language.name}"
