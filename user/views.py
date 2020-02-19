from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from user.helpers import get_role
from user.mixins import LoginRequiredMixin
from organization.models import Faculty

class StudentUserSettingsView(LoginRequiredMixin, View):
    """
    学生用户个人设置
    """
    def get(self, request):
        role_str, role_obj = get_role(request.user)
        
        student = self.get_student_info(request.user, role_obj)
        facultys = self.get_faculty_list()
        context = {
            "student": student,
            'facultys': facultys
        }
        return render(request, 'student_settings.html', context)

    def post(self, request):
        pass

    def get_student_info(self, user, role):
        """
        获取学生信息，返回一个学生信息字典
        user: auth_user 账号
        role: 账号角色对象，即student实例
        """
        student = {}
        student['username'] = user.username
        student['name']  = role.name
        student['phone'] = role.phone
        student['gender'] = role.gender
        student['qq'] = role.qq
        student['email'] = user.email
        student['faculty'] = role.faculty
        student['profession'] = role.profession
        student['direction'] = role.diretcion
        student['klass'] = role.klass

        return student

    def get_faculty_list(self):
        """
        获取学院列表对象
        """
        faculty_list = Faculty.objects.all()
        return faculty_list
