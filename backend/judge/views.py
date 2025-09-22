from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED
# ---------- JUDGE0 INTEGRATION DEPENDENCIES ----------
import http.client
from dotenv import load_dotenv
import os,json
# ---------- JUDGE0 INTEGRATION DEPENDENCIES ----------
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
    http_method_names = ['POST']
    def create(self, request, *args, **kwargs):
        try:
            data = {}
            data['problem'] = self.request.data['problem']
            # ---------- FROM JUDGE0 DOCUMENTATION BELOW: GETTING SUBMISSION TOKEN ----------
            conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
            payload = json.dumps({
                "language_id": 92,
                "source_code": f'{self.request.data['submitted_solution']}',
                "stdin": "",
                "expected_output":""
            })
            load_dotenv()
            headers = {
                'x-rapidapi-key': os.getenv('KEY'),
                'x-rapidapi-host': "judge0-ce.p.rapidapi.com",
                'Content-Type': "application/json"
            }
            conn.request("POST", "/submissions?base64_encoded=false&wait=false&fields=*", payload, headers)
            res = conn.getresponse()
            data = res.read()
            submission_token = json.loads(data.decode('utf-8'))['token']
            # ---------- FROM JUDGE0 DOCUMENTATION ABOVE: GETTING SUBMISSION TOKEN ----------
            # ---------- FROM JUDGE0 DOCUMENTATION BELOW: GETTING SUBMISSION RESULT ----------
            conn1 = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
            headers1 = {
                'x-rapidapi-key': os.getenv('KEY'),
                'x-rapidapi-host': "judge0-ce.p.rapidapi.com"
            }
            conn1.request("GET", f"/submissions/{submission_token}?base64_encoded=false&fields=*", headers=headers1)
            res1 = conn.getresponse()
            data1 = res1.read()
            result_json = json.loads(data1.decode('utf-8'))
            # ---------- FROM JUDGE0 DOCUMENTATION ABOVE: GETTING SUBMISSION RESULT ----------
            data['submitted_solution'] = f'{result_json}'
            if result_json['expected_output']==result_json['stdout']:
                data['status'] = Status.objects.get(code=1).id
            else:
                data['status'] = Status.objects.get(code=0).id
            serializer = SubmissionSerializer(data=data)
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