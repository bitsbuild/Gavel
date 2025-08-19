from django.contrib.admin import site
from judge.models import Language,Set,Challenge,TestCase,Submission
site.register(Language)
site.register(Set)
site.register(Challenge)
site.register(TestCase)
site.register(Submission)
