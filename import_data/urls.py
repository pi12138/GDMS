from django.conf.urls import url
from .views import ImportData

urlpatterns = [
    url('', ImportData.as_view(), name='data'),
]