from rest_framework.routers import DefaultRouter
from judge.views import LanguageViewSet
router = DefaultRouter()
router.register(r'languages',LanguageViewSet,basename='languages')
urlpatterns = router.urls