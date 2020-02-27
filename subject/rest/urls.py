from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from subject.rest.views import PendingSubjectViewSet, PassedSubjectViewSet, SelectSubjectViewSet


router = DefaultRouter()
router.register(r'pending_subject', PendingSubjectViewSet, "pending-subject")
router.register(r'passed_subject', PassedSubjectViewSet, 'passed-subject')
router.register(r'select_subject', SelectSubjectViewSet, 'select-subject')

urlpatterns = router.urls
