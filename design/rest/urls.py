from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from design.rest.views import GraduationDesignViewSet


router = DefaultRouter()
# router.register('', ReportViewSet, 'api-report')
router.register('design', GraduationDesignViewSet, 'api-design')

urlpatterns = router.urls


