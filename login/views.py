from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse
# Create your views here.
from user.helpers import get_role


class LoginView(View):
    """
    登录视图
    """
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        queryset = User.objects.filter(username=username)

        if not queryset.exists():
            return render(request, 'login.html', {'error_msg': "该账号不存在！"})
        
        user = queryset[0]
        if not user.check_password(password):
            return render(request, 'login.html', {'error_msg': "用户密码错误！"})
        
        role_str, role_obj = get_role(user)
        role_dict = {
            "teacher": "teacher_home.html", 
            "student": "student_home.html",
            "administrator": "administrator_home.html",
        }
        
        if not role_str:
            return render(request, 'login.html', {'error_msg': "账户异常！"})

        return render(request, role_dict[role_str], context={'role_obj': role_obj})
        

class LogoutView(View):
    """
    登出
    """
    def get(self, request):
        logout(request)

        return redirect(reverse('login:login'))