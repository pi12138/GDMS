from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from design.rest.serializers import GraduationDesignSerializer, GraduationThesisSerializer
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
        query_dict = request.data
        data = dict()
        data['design'] = query_dict.get('file')
        data['upload_time'] = datetime.datetime.now()
        data['subject'] = request.user.student.select_student.id

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
        ret = self.handle_pk(pk)
        if ret == dict:
            return Response(ret, status=400)

        query_dict = request.data
        data = dict()
        data['design'] = query_dict.get('file')
        data['upload_time'] = datetime.datetime.now()
        data['subject'] = request.user.student.select_student.id
        ser = GraduationDesignSerializer(instance=ret, data=data)

        if not ser.is_valid():
            return Response({"msg": "修改毕业设计失败", 'error': ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def partial_update(self, request, pk=None):
        """
        教师功能：审阅毕业设计
        """
        ret = self.handle_pk(pk)
        if ret == dict:
            return Response(ret, status=400)

        data = request.data
        data['review_time'] = datetime.datetime.now()

        ser = GraduationDesignSerializer(instance=ret, data=data)
        if not ser.is_valid():
            return Response({"msg": "审核毕业设计失败", 'error': ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def handle_pk(self, pk):
        if not pk:
            return {'msg': "未传入毕业设计参数"}

        query_set = GraduationDesign.objects.filter(pk=pk)
        if not query_set.exists():
            return {'msg': "毕业设计不存在"}

        return query_set[0]


class GraduationThesisViewSet(ViewSet):
    """
    通用功能: 毕业论文
        - 学生: 上传 + 下载 + 修改
        - 教师: 审核 + 下载
        - 管理员: 查看
    """
    def create(self, request):
        """
        学生功能: 上传毕业论文
        """
        query_dict = request.data
        data = dict()
        data['thesis'] = query_dict.get('file')
        data['key_words'] = query_dict.get('key_words')
        data['summary'] = query_dict.get('summary')
        data['subject'] = request.user.student.select_student.id
        data['upload_time'] = datetime.datetime.now()

        ser = GraduationThesisSerializer(data=data)
        if not ser.is_valid():
            return Response({"msg": "创建毕业论文失败", 'error': ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def retrieve(self, request, pk=None):
        """
        通用功能: 查看毕业设计
        """
        ret = self.handle_pk(pk)
        if ret == dict:
            return Response(ret, status=400)

        ser = GraduationThesisSerializer(instance=ret)

        return Response({"data": ser.data})

    def update(self, request, pk=None):
        """
        学生功能: 修改毕业论文
        """
        ret = self.handle_pk(pk)
        if ret == dict:
            return Response(ret, status=400)

        query_dict = request.data
        data = dict()
        data['thesis'] = query_dict.get('file')
        data['key_words'] = query_dict.get('key_words')
        data['summary'] = query_dict.get('summary')
        data['subject'] = request.user.student.select_student.id
        data['upload_time'] = datetime.datetime.now()

        ser = GraduationThesisSerializer(instance=ret, data=data)
        if not ser.is_valid():
            return Response({'msg': "更新毕业论文失败"}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def partial_update(self, request, pk=None):
        """
        教师功能: 审核毕业设计
        """
        ret = self.handle_pk(pk)
        if ret == dict:
            return Response(ret, status=400)

        data = request.data
        data['review_time'] = datetime.datetime.now()

        ser = GraduationThesisSerializer(instance=ret, data=data)
        if not ser.is_valid():
            return Response({'msg': "审核毕业论文失败"}, status=400)

        ser.save()
        return Response({'data': ser.data})


def handle_pk(self, pk):
        if not pk:
            return {'msg': "未传入毕业论文参数"}

        query_set = GraduationDesign.objects.filter(pk=pk)
        if not query_set.exists():
            return {'msg': "毕业沦为不存在"}

        return query_set[0]
