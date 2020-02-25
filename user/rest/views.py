from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from user.rest.serializers import TeacherSettingsSerializer


class TeacherSettingsViewSet(ViewSet):
    """
    教师设置
    """
    def list(self, request):
        teacher = request.user.teacher
        ser = TeacherSettingsSerializer(instance=teacher)
        return Response(ser.data)
