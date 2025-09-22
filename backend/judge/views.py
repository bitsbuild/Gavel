from rest_framework.viewsets import ModelViewSet
from judge.models import (
    Language,
    Problem,
    ProblemSet,
    ProblemInputOutput,
    ProblemSetMapping,
    Status,
    Submission)
from judge.serializer import (
    LanguageSerializer,
    ProblemSerializer,
    ProblemSetSerializer,
    ProblemInputOutputSerializer,
    ProblemSetMappingSerializer,
    StatusSerializer,
    SubmissionSerializer)
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
class ProblemSetViewSet(ModelViewSet):
    queryset = ProblemSet.objects.all()
    serializer_class = ProblemSetSerializer
class ProblemInputOutputViewSet(ModelViewSet):
    queryset = ProblemInputOutput.objects.all()
    serializer_class = ProblemInputOutputSerializer
class ProblemSetMappingViewSet(ModelViewSet):
    queryset = ProblemSetMapping.objects.all()
    serializer_class = ProblemSetMappingSerializer
class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer