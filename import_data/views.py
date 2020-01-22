from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse

from .helpers import handle_excel_info
from organization.models import Faculty
# Create your views here.


class ImportFaculty(View):
    """
    导入学院信息
    """
    def get(self, request):
        return render(request, 'import_faculty.html')

    def post(self, request):
        faculty_info = request.FILES.get('faculty_info', None)

        if not faculty_info:
            info = "请传入文件"

        try:
            data_list = handle_excel_info(faculty_info.read())
            for data in data_list:
                Faculty.objects.create(name=data[0], number=data[1], monitor=data[2])
        except Exception as e:
            info = "文件内容存在异常"
            print('error info: {}'.format(e))

        info = '导入成功'
        context = {
            'info': info
        }

        return render(request, 'import_faculty.html', context)
