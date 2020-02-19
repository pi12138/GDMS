from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from user.helpers import get_role

class StudentUserSettingsView(View):
    """
    学生用户个人设置
    """
    def get(self, request):
        role_str, role_obj = get_role(request.user)

        context = {
            'role_obj': role_obj
        }
        return render(request, 'student_settings.html')

    def post(self, request):
        pass