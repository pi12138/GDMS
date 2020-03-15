from django.conf.urls import url

from announcement.views import AnnouncementView


urlpatterns = [
    # url(r'^student_settings/$', StudentUserSettingsView.as_view(), name='student-settings'),
    url(r'^announcement/$', AnnouncementView.as_view(), name='announcement'),
]
