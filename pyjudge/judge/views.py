from judge.models import (Language,
                          Set,
                          Challenge,
                          TestCase,
                          Submission)
from judge.serializers import (LanguageSerializer,
                               SetSerializer,
                               ChallengeSerializer,
                               TestCaseSerializer,
                               SubmissionSerializer)
from rest_framework.viewsets import ModelViewSet
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
class SetViewSet(ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
class TestCaseViewSet(ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer