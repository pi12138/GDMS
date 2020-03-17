from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from message_board.models import MessageBoard
from message_board.rest.serializers import MessageBoardSerializer

import datetime


class MessageBoardViewSet(ViewSet):
    """
    留言板功能:
        - 学生: 发表 + 查案
        - 教师: 查看 + 发表
        - 管理员: 查看
    """
    def list(self, request):
        """
        留言列表
        """
        pass

    def retrieve(self, request, pk=None):
        """
        单个留言详情
        """
        if not pk:
            return Response({'msg': "未传入消息参数"}, status=400)

        query_set = MessageBoard.objects.filter(pk=pk)
        if not query_set.exists():
            return Response({'msg': "该留言不存在"}, status=400)

        ser = MessageBoardSerializer(instance=query_set[0])

        return Response({'data': ser.data})

    def create(self, request):
        """
        创建留言
        """
        query_dict = request.data
        student = request.user.student
        teacher = self.get_instructor(student)

        if not teacher:
            return Response({'msg': "创建留言失败", 'error': "未找到指导老师"}, status=400)

        data = dict()
        data['title'] = query_dict.get('title')
        data['content'] = query_dict.get('content')
        data['annex'] = query_dict.get('file', None)
        data['publish_time'] = datetime.datetime.now()
        data['publisher'] = student.id
        data['receiver'] = teacher.id

        ser = MessageBoardSerializer(data=data)
        if not ser.is_valid():
            return Response({"msg": "创建留言失败", 'error': ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    @action(methods=["GET"])
    def read_message(self, request, pk=None):
        """设置消息未已读"""
        if not pk:
            return Response({'msg': "未传入消息参数"}, status=400)

        query_set = MessageBoard.objects.filter(pk=pk)
        if not query_set.exists():
            return Response({'msg': "该留言不存在"}, status=400)

        obj = query_set[0]
        obj.is_read = True
        obj.save()
        return Response({'msg': "设置成功"})

    @action(methods=['POST'])
    def reply_message(self, request, pk=None):
        """回复留言"""
        if not pk:
            return Response({'msg': "未传入消息参数"}, status=400)

        query_set = MessageBoard.objects.filter(pk=pk)
        if not query_set.exists():
            return Response({'msg': "该留言不存在"}, status=400)

        query_dict = request.data
        teacher = request.user.teacher

        data = dict()
        data['title'] = query_dict.get('title')
        data['content'] = query_dict.get('content')
        data['annex'] = query_dict.get('file', None)
        data['publish_time'] = datetime.datetime.now()
        data['publisher'] = teacher.id
        data['receiver'] = query_dict.get('receiver')

        ser = MessageBoardSerializer(data=data)
        if not ser.is_valid():
            return Response({"msg": "创建回复失败", 'error': ser.errors}, status=400)

        ser.save()
        return Response({'data': ser.data})

    def get_instructor(self, student):
        """获取指导老师"""
        if hasattr(student, 'select_student'):
            return student.select_student.questioner
        return None
