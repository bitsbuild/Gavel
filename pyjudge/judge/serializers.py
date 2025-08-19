from judge.models import (Language,
                          Set,
                          Challenge,
                          TestCase,
                          Submission)
from rest_framework.serializers import ModelSerializer,SlugRelatedField,StringRelatedField
class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
class SetSerializer(ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
class ChallengeSerializer(ModelSerializer):
    challenge_set = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field = 'name'
    )
    class Meta:
        model = Challenge
        fields = '__all__'
class TestCaseSerializer(ModelSerializer):
    language = StringRelatedField()
    challenge = StringRelatedField()
    class Meta:
        model = TestCase
        fields = '__all__'
class SubmissionSerializer(ModelSerializer):
    language = StringRelatedField()
    challenge = StringRelatedField()
    user = StringRelatedField()
    class Meta:
        model = Submission
        fields = '__all__'