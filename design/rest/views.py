from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from design.rest.serializers import GraduationDesignSerializer
from design.models import GraduationDesign

import datetime


class GraduationDesignViewSet(ViewSet):
    """
    毕业设计视图： 通用功能
        - 学生： 上传毕业设计文件
        - 教师： 下载毕业设计文件 + 审阅毕业设计
        - 管理员： 查看毕业设计
    """

    def create(self, request):
        """
        学生功能： 上传毕业设计
        """
        data = request.data
        data['upload_time'] = datetime.datetime.now()

        ser = GraduationDesignSerializer(data=data)
        if not ser.is_valid():
            return Response({'msg': "上传失败", 'error': ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def retrieve(self, request, pk=None):
        """
        通用功能： 查看毕业设计
        """
        ret = self.handle_pk(pk)
        if ret == dict:
            return Response(ret, status=400)

        ser = GraduationDesignSerializer(instance=ret)

        return Response({'data': ser.data})

    def update(self, request, pk=None):
        """
        学生功能：修改毕业设计
        """
        pass

    def partial_update(self, request, pk=None):
        """
        教师功能：审阅毕业设计
        """
        pass

    def handle_pk(self, pk):
        if not pk:
            return {'msg': "未传入毕业设计参数"}

        query_set = GraduationDesign.objects.filter(pk=pk)
        if not query_set.exists():
            return {'msg': "毕业设计不存在"}

        return query_set[0]
