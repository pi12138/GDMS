from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from report.rest.serializers import ReportSerializer


class ReportViewSet(ViewSet):
    """
    通用功能： 开题报告视图
        - 学生： 编写+修改+查看
        - 教师： 审阅 + 查看
        - 管理员： 查看
    """
    def create(self, request):
        data = request.data

        ser = ReportSerializer(data=data)
        if not ser.is_valid():
            return Response({"msg": "创建失败", "error": ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})
