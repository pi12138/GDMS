from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from user.rest.serializers import TeacherSettingsSerializer
from user.models import Teacher
from subject.models import TaskBook


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
        与学生相关的一些信息： 课题， 任务书
        """
        user = request.user.student

        subject = None
        task_book = None
        if hasattr(user, 'select_student'):
            subject = user.select_student

        if subject:
            query_set = TaskBook.objects.filter(subject_id=subject.id, review_result=1)
            task_book = query_set[0] if query_set.exists() else None

        res = {
            'subject_id': subject.id,
            'task_book_id': task_book.id
        }

        return Response(res)
