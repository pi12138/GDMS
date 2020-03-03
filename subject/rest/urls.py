from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from subject.rest.views import PendingSubjectViewSet, PassedSubjectViewSet, SelectSubjectViewSet, \
    ApprovalApplicationViewSet, SubjectViewSet
from subject.rest.views import my_subject


router = DefaultRouter()
router.register(r'pending_subject', PendingSubjectViewSet, "api-pending-subject")
router.register(r'passed_subject', PassedSubjectViewSet, 'api-passed-subject')
router.register(r'select_subject', SelectSubjectViewSet, 'api-select-subject')
router.register(r'approval_application', ApprovalApplicationViewSet, 'api-approval-application')
router.register(r'', SubjectViewSet, 'api-subject')

urlpatterns = router.urls

urlpatterns = [
    url(r'^my_subject/$', my_subject, name='my-subject'),
] + urlpatterns

