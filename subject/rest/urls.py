from django.conf.urls import url

from subject.rest.views import PendingSubjectView

urlpatterns = [
    # url(r'^student_settings/$', StudentUserSettingsView.as_view(), name='student-settings'),
    url(r'^pending_subject/$', PendingSubjectView.as_view(), name='pending-subject'),
]