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
from judge.models import Language,Challenge
import os
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
    def create(self, request, *args, **kwargs):
        data = {
            "user":request.user.id,
            "challenge":request.data['challenge'],
            "language":request.data['language'],
        }
        language_instance = Language.objects.get(pk=data['language'])
        challenge_instance = Challenge.objects.get(pk=data['challenge'])
        serialier = self.get_serializer(data=data)
        serialier.is_valid(raise_exception=True)
        self.perform_create(serializer)
        file_ext = os.path.splitext(serialier.validated_data['solution_file'].name)[1]
        solution_file_path = f"{challenge_instance.name}/{language_instance.name}{file_ext}"
        test_case_file_path = f"{challenge_instance.name}/{request.user.username}/{language_instance.name}{file_ext}"
        
