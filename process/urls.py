from django.conf.urls import url

from .views import TeacherProcess


urlpatterns = [
    # url(r'^student_settings/$', StudentUserSettingsView.as_view(), name='student-settings'),
    url(r'^teacher/$', TeacherProcess.as_view(), name='teacher'),
]
