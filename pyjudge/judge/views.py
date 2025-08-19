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
    model = Language
    serializer_class = LanguageSerializer
class SetViewSet(ModelViewSet):
    model = Set
    serializer_class = SetSerializer
class ChallengeViewSet(ModelViewSet):
    model = Challenge
    serializer_class = ChallengeSerializer
class TestCaseViewSet(ModelViewSet):
    model = TestCase
    serializer_class = TestCaseSerializer
class SubmissionViewSet(ModelViewSet):
    model = Submission
    serializer_class = SubmissionSerializer