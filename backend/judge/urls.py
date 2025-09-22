from rest_framework.routers import DefaultRouter
from judge.views import (
    LanguageViewSet,
    ProblemViewSet,
    ProblemSetViewSet,
    ProblemInputOutputViewSet,
    ProblemSetMappingViewSet,
    StatusViewSet,
    SubmissionViewSet)
router = DefaultRouter()
router.register(r'languages',LanguageViewSet,basename='languages')
router.register(r'problems',ProblemViewSet,basename='problems')
router.register(r'sets',ProblemSetViewSet,basename='sets')
router.register(r'submissions',SubmissionViewSet,basename='submissions')
router.register(r'statuses',StatusViewSet,basename='statuses')
router.register(r'problem_input_output',ProblemInputOutputViewSet,basename='problem_input_output')
router.register(r'problem_set_mapping',ProblemSetMappingViewSet,basename='problem_set_mapping')
urlpatterns = router.urls