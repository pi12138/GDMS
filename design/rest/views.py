from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


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
        学生功能： 创建毕业设计
        """
        pass