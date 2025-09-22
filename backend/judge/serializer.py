from rest_framework.serializers import ModelSerializer
from judge.models import (
    Language,
    Problem,
    ProblemSet,
    ProblemInputOutput,
    ProblemSetMapping,
    Status,
    Submission)
class LangaugeSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
class ProblemSetSerializer(ModelSerializer):
    class Meta:
        model = ProblemSet
        fields = '__all__'
class ProblemInputOutputSerialzier(ModelSerializer):
    class Meta:
        model = ProblemInputOutput
        fields = '__all__'
class ProblemSetMappingSerializer(ModelSerializer):
    class Meta:
        model = ProblemSetMapping
        fields = '__all__'
class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'