from django.conf.urls import url

from .views import StudentUserSettingsView, AdminSettings, TeacherSettings
from .views import change_password


urlpatterns = [
    url(r'^student_settings/$', StudentUserSettingsView.as_view(), name='student-settings'),
    url(r'^change_password/$', change_password, name="change_password"),
    url(r'^administrator_settings/$', AdminSettings.as_view(), name='admin-settings'),
    url(r'^teacher_settings/$', TeacherSettings.as_view(), name='teacher-settings'),
]
