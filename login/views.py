from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class LoginView(View):
    """
    登录视图
    """
    def get(self, request):
        return render(request, 'login.html')


