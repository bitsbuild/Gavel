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
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class SetViewSet(ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]   
    filterset_fields = []
    search_fields = filterset_fields
    ordering_fields = filterset_fields 
class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class TestCaseViewSet(ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []
    search_fields = filterset_fields
    ordering_fields = filterset_fields