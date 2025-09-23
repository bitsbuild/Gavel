from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# ---------- JUDGE0 INTEGRATION DEPENDENCIES ----------
import http.client
from dotenv import load_dotenv
import os,json
# ---------- JUDGE0 INTEGRATION DEPENDENCIES ----------
from judge.models import (
    Language,
    Problem,
    ProblemSet,
    ProblemSetMapping,
    Status,
    Submission)
from judge.serializer import (
    LanguageSerializer,
    ProblemSerializer,
    ProblemSetSerializer,
    ProblemSetMappingSerializer,
    StatusSerializer,
    SubmissionSerializer)
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]
class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [IsAdminUser]
class ProblemSetViewSet(ModelViewSet):
    queryset = ProblemSet.objects.all()
    serializer_class = ProblemSetSerializer
    permission_classes = [IsAdminUser]
class ProblemSetMappingViewSet(ModelViewSet):
    queryset = ProblemSetMapping.objects.all()
    serializer_class = ProblemSetMappingSerializer
    permission_classes = [IsAdminUser]
class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]
class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        try:
            pass_data = {}
            pass_data['problem'] = self.request.data['problem']
            pass_data['language'] = self.request.data['language']
            problem = Problem.objects.get(pk=pass_data['problem'])
            # ---------- FROM JUDGE0 DOCUMENTATION BELOW: GETTING SUBMISSION TOKEN ----------
            conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
            payload = json.dumps({
                "language_id": Language.objects.get(pk=pass_data['language']).code,
                "source_code": self.request.data['submitted_solution'],
                "stdin": f"{problem.problem_input}",
                "expected_output":f"{problem.problem_expected_output}"
            })
            load_dotenv()
            headers = {
                'x-rapidapi-key': os.getenv('KEY'),
                'x-rapidapi-host': "judge0-ce.p.rapidapi.com",
                'Content-Type': "application/json"
            }
            conn.request("POST", "/submissions?base64_encoded=false&wait=true&fields=*", payload, headers)
            res = conn.getresponse()
            data = res.read()
            submission_token = json.loads(data.decode('utf-8'))['token']
            # ---------- FROM JUDGE0 DOCUMENTATION ABOVE: GETTING SUBMISSION TOKEN ----------
            # ---------- FROM JUDGE0 DOCUMENTATION BELOW: GETTING SUBMISSION RESULT ----------
            conn_ = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
            headers_ = {
                'x-rapidapi-key': os.getenv('KEY'),
                'x-rapidapi-host': "judge0-ce.p.rapidapi.com"
            }
            conn_.request("GET", f"/submissions/{submission_token}?base64_encoded=false&fields=*", headers=headers_)
            res_ = conn_.getresponse()
            data_ = res_.read()
            result_json = json.loads(data_.decode('utf-8'))
            # ---------- FROM JUDGE0 DOCUMENTATION ABOVE: GETTING SUBMISSION RESULT ----------
            pass_data['submitted_solution'] = f'{result_json}'
            pass_data['user'] = self.request.user.pk
            if result_json['status_id']==3:
                pass_data['status'] = str(Status.objects.get(code=1).id)
            elif result_json['status_id']==4:
                pass_data['status'] = str(Status.objects.get(code=0).id)
            print(pass_data)
            serializer = SubmissionSerializer(data=pass_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {
                    'Status':'Submission Created Successfully',
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