from django.shortcuts import render
from django.views import View
# Create your views here.
from user.mixins import LoginRequiredMixin


class TeacherProcess(LoginRequiredMixin, View):
    """
    教师功能: 毕业设计过程页面
    """
    def get(self, request):
        return render(request, 'teacher_process.html')
