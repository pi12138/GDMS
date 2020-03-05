from rest_framework.routers import DefaultRouter

from user.rest.views import TeacherSettingsViewSet, StudentInfoViewSet


router = DefaultRouter()
router.register(r'teacher_settings', TeacherSettingsViewSet, 'api-teacher-settings')
router.register(r'student_info', StudentInfoViewSet, 'api-student-info')

urlpatterns = router.urls
