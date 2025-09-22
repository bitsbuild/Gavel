from rest_framework.viewsets import ModelViewSet
from judge.models import Language
from judge.serializer import LangaugeSerializer
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LangaugeSerializer