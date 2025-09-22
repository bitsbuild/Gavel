from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from judge.models import (
    Language,
    Problem,
    ProblemSet,
    ProblemInputOutput,
    ProblemSetMapping,
    Status,
    Submission)
from judge.serializer import (
    LanguageSerializer,
    ProblemSerializer,
    ProblemSetSerializer,
    ProblemInputOutputSerializer,
    ProblemSetMappingSerializer,
    StatusSerializer,
    SubmissionSerializer)
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
class ProblemSetViewSet(ModelViewSet):
    queryset = ProblemSet.objects.all()
    serializer_class = ProblemSetSerializer
class ProblemInputOutputViewSet(ModelViewSet):
    queryset = ProblemInputOutput.objects.all()
    serializer_class = ProblemInputOutputSerializer
class ProblemSetMappingViewSet(ModelViewSet):
    queryset = ProblemSetMapping.objects.all()
    serializer_class = ProblemSetMappingSerializer
class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    def create(self, request, *args, **kwargs):
        try:
            serializer = SubmissionSerializer(data={})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {
                    'Status':'Submission Created Successfully',
                    'Error':str(e)
                },
                status=HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    'Status':'Error',
                    'Error':str(e)
                },
                status=HTTP_400_BAD_REQUEST
            )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)