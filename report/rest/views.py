from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from report.rest.serializers import ReportSerializer

from report.models import Report

import datetime


class ReportViewSet(ViewSet):
    """
    通用功能： 开题报告视图
        - 学生： 编写+修改+查看
        - 教师： 审阅 + 查看
        - 管理员： 查看
    """
    def create(self, request):
        """
        学生功能: 编写开题报告
        """
        data = request.data
        data['submit_time'] = datetime.datetime.now()
        data['subject'] = request.user.student.select_student.id

        ser = ReportSerializer(data=data)
        if not ser.is_valid():
            return Response({"msg": "创建失败", "error": ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def retrieve(self, request, pk=None):
        if not pk:
            return Response({'msg': "未传入开题报告参数"}, status=400)

        query_set = Report.objects.filter(id=pk)
        if not query_set.exists():
            return Response({'msg': "开题报告不存在"}, status=400)

        ser = ReportSerializer(instance=query_set[0])

        return Response({'data': ser.data})
