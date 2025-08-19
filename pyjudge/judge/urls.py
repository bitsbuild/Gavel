from rest_framework.routers import DefaultRouter
from judge.views import (
    LanguageViewSet,
    SetViewSet,
    ChallengeViewSet,
    TestCaseViewSet,
    SubmissionViewSet
)
router = DefaultRouter()
router.register("language",LanguageViewSet,basename="language")
router.register("set",SetViewSet,basename="set")
router.register("challenge",ChallengeViewSet,basename="challenge")
router.register("testcase",TestCaseViewSet,basename="testcase")
router.register("submission",SubmissionViewSet,basename="submission")
urlpatterns = router.urls

