from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from user.rest.serializers import TeacherSettingsSerializer
from user.models import Teacher


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
