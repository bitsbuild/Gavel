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
from rest_framework.permissions import IsAdminUser,IsAuthenticated
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]
class SetViewSet(ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    permission_classes = [IsAdminUser]
class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAdminUser]
class TestCaseViewSet(ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAdminUser]
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]