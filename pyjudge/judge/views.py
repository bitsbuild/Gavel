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
    filterset_fields = ['id','name','created','updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class SetViewSet(ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]   
    filterset_fields = ['id','name','created','updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields 
class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = fields = ["id","name","challenge_body","constraints","input_instruction","output_instruction","code_format","challenge_set","created","updated"]
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class TestCaseViewSet(ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = fields = ["id","language","challenge","created","updated"]
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id","user","challenge","language","outcome","number_of_test_cases","created","updated"]
    search_fields = filterset_fields
    ordering_fields = filterset_fields