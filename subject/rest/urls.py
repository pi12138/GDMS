from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from subject.rest.views import PendingSubjectViewSet, PassedSubjectViewSet, SelectSubjectViewSet
from subject.rest.views import my_subject


router = DefaultRouter()
router.register(r'pending_subject', PendingSubjectViewSet, "pending-subject")
router.register(r'passed_subject', PassedSubjectViewSet, 'passed-subject')
router.register(r'select_subject', SelectSubjectViewSet, 'select-subject')

urlpatterns = router.urls

urlpatterns = [
    url(r'^my_subject/$', my_subject, name='my-subject'),
] + urlpatterns

