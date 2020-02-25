from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from subject.rest.views import PendingSubjectViewSet, PassedSubjectViewSet


router = DefaultRouter()
router.register(r'pending_subject', PendingSubjectViewSet, "pending-subject")
router.register(r'passed_subject', PassedSubjectViewSet, 'passed-subject')

urlpatterns = router.urls
