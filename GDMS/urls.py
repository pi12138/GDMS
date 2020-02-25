"""GDMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('login.urls', 'login'), namespace='login')),
    path("user/", include(('user.urls', 'user'), namespace="user")),
    path("organization/", include(("organization.urls", "organization"), namespace="organization")),
    path("subject/", include(("subject.urls", "subject"), namespace="subject")),
    # url(r'^login/', obtain_jwt_token),

    path('import_data/', include(('import_data.urls', 'import_data'), namespace='import_data')),

    # path('api/login/', include(('login.rest.urls', 'login'), namespace='api-login')),
    path('api/subject/', include(('subject.rest.urls', 'subject'), namespace='api-subject')),
    path('api/user/', include(('user.rest.urls', 'user'), namespace='api-user')),
]
