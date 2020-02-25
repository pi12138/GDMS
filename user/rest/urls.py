from rest_framework.routers import DefaultRouter

from user.rest.views import TeacherSettingsViewSet


router = DefaultRouter()
router.register(r'teacher_settings', TeacherSettingsViewSet, 'teacher-settings')

urlpatterns = router.urls
