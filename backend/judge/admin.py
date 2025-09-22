from django.contrib import admin
from judge.models import Language,Problem,ProblemSet,ProblemSetMapping,Status,Submission
admin.site.register(Language)
admin.site.register(Problem)
admin.site.register(ProblemSet)
admin.site.register(ProblemSetMapping)
admin.site.register(Status)
admin.site.register(Submission)