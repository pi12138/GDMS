from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from user.rest.serializers import TeacherSettingsSerializer, SelectedStudentSerializer
from user.models import Teacher, Student
from subject.models import TaskBook, Subject
from report.models import Report
from design.models import GraduationDesign, GraduationThesis
from user.helpers import get_role
from announcement.rest.paginations import CustomPageiantion


class TeacherSettingsViewSet(ViewSet):
    """
    教师设置
    """
    def list(self, request):
        teacher = request.user.teacher
        ser = TeacherSettingsSerializer(instance=teacher)
        return Response(ser.data)

    def update(self, request, pk=None):
        tea = Teacher.objects.filter(id=pk)
        if not tea.exists():
            return Response("该用户不存在", status=400)

        tea = tea[0]
        data = request.data
        user = request.user

        ser = TeacherSettingsSerializer(instance=tea, data=data)
        if not ser.is_valid():
            return Response("传入数据不合法！", status=400)

        user.email = data.get('email', None)
        user.save()
        ser.save()

        return Response(ser.data)


class StudentInfoViewSet(ViewSet):
    """
    学生功能： 学生信息
    """

    @action(detail=False)
    def related_info(self, request):
        """
        与学生相关的一些信息： 课题ID， 任务书ID, 开题报告ID
        """
        user = request.user.student

        subject = None
        task_book = None
        report = None
        design = None
        thesis = None
        if hasattr(user, 'select_student'):
            subject = user.select_student

        if subject:
            subject_id = subject.id

            query_set = TaskBook.objects.filter(subject_id=subject_id, review_result=1)
            task_book = query_set[0] if query_set.exists() else None

            query_set = Report.objects.filter(subject_id=subject_id)
            report = query_set[0] if query_set.exists() else None

            query_set = GraduationDesign.objects.filter(subject_id=subject_id)
            design = query_set[0] if query_set.exists() else None

            query_set = GraduationThesis.objects.filter(subject_id=subject_id)
            thesis = query_set[0] if query_set.exists() else None

        res = {
            'subject_id': subject.id if subject else None,
            'subject_name': subject.subject_name if subject else None,
            'task_book_id': task_book.id if task_book else None,
            'report_id': report.id if report else None,
            'design_id': design.id if design else None,
            'thesis_id': thesis.id if thesis else None,
        }

        return Response(res)


class UserInfoViewSet(ViewSet):
    """
    用户信息
    """

    def list(self, request):
        user = request.user

        role_str, role_obj = get_role(auth_user=user)

        if role_str == 'student':
            return self.student_info(role_obj)
        elif role_str == 'teacher':
            return self.teacher_info(role_obj)
        elif role_str == 'administrator':
            return Response({'role': 'administrator'})

    def student_info(self, role):
        res_data = {
            'role': 'student',
            'user_id': role.account_id,
            'student_id': role.id,
            'student_name': role.name,
            'guide_teacher_id': 0,
            'guide_teacher_name': "",
            'guide_teacher_user_id': 0
        }

        if hasattr(role, 'select_student'):
            teacher = role.select_student.questioner
            res_data['guide_teacher_id'] = teacher.id
            res_data['guide_teacher_name'] = teacher.name
            res_data['guide_teacher_user_id'] = teacher.account_id

        return Response(res_data)

    def teacher_info(self, role):
        res_data = {
            'role': 'teacher',
            'user_id': role.account_id,
            'teacher_id': role.id,
            'teacher_name': role.name,
            'guided_students': None
        }

        query_set = role.subject_set.filter(select_student__isnull=False).select_related('select_student')
        students = list()
        for i in query_set:
            student_info = {
                'student_id': i.select_student_id,
                'student_name': i.select_student.name,
                'student_user_id': i.select_student.account_id
            }
            students.append(student_info)

        if len(students) > 0:
            res_data['guided_students'] = students

        return Response(res_data)


class SelectedStudentViewSet(ViewSet):
    """
    已选题学生列表
    """

    def list(self, request):
        query_set = Subject.objects.filter(select_student__isnull=False)
        student_list = [i.select_student for i in query_set]

        page_obj = CustomPageiantion()
        data = page_obj.paginate_queryset(queryset=student_list, request=request, view=self)
        ser = SelectedStudentSerializer(instance=data, many=True)

        return page_obj.get_paginated_response(ser.data)
