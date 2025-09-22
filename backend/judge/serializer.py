from rest_framework.serializers import ModelSerializer
from judge.models import Language
class LangaugeSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'