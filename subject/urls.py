from django.conf.urls import url

from .views import DeclareSubject, AlterSubject, ApprovalSubject


urlpatterns = [
    # url(r'^student_settings/$', StudentUserSettingsView.as_view(), name='student-settings'),
    url(r"^declare_subject/$", DeclareSubject.as_view(), name="declare-subject"),
    url(r"^alter_subject/$", AlterSubject.as_view(), name="alter-subject"),
    url(r'^approval_subject/$', ApprovalSubject.as_view(), name="approval-subject"),
]