from django.conf.urls import url
from .views import ImportFaculty

urlpatterns = [
    url('^faculty/$', ImportFaculty.as_view(), name='faculty'),
]