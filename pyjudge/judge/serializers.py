from judge.models import Language,Set,Challenge,TestCase,Submission
from rest_framework.serializers import ModelSerializer
class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
class SetSerializer(ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
class ChallengeSerializer(ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
class TestCaseSerializer(ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'
class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'