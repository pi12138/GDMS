from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from subject.rest.views import PendingSubjectViewSet


router = DefaultRouter()
router.register(r'pending_subject', PendingSubjectViewSet, "pending-subject")

urlpatterns = router.urls
