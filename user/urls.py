from django.conf.urls import url

from .views import StudentUserSettingsView


urlpatterns = [
    url(r'^student_settings/$', StudentUserSettingsView.as_view(), name='student-settings'),
]