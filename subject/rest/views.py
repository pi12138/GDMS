from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import datetime

from django.core.paginator import Paginator
from django.db.models import Q

from subject.models import Subject
from .serializers import SubjectSerializer


class PendingSubjectViewSet(ViewSet):
    """
    管理员功能： 待审批课题
    """

    def list(self, request):

        query_set = Subject.objects.filter(review_result=0).order_by('-declare_time')
        ser = SubjectSerializer(instance=query_set, many=True)
        res = self.pagination(ser.data, request)

        return Response(res)

    def partial_update(self, request, pk=None):

        data = request.data
        subjects = Subject.objects.filter(id=pk)
        if not subjects.exists():
            return Response({'error': '当前课题不存在！'}, status=400)

        data['reviewer'] = request.user.administrator.id
        data['review_time'] = datetime.datetime.now()

        ser = SubjectSerializer(instance=subjects[0], data=data)
        if not ser.is_valid():
            return Response({'error': "发生错误", 'error_code': ser.errors}, status=400)

        ser.save()
        return Response({'resheader is not definedults': ser.data, 'msg': '审核成功'})

    @staticmethod
    def pagination(data, request):
        page = request.query_params.get('page', 1)
        page = int(page)
        path = request.path

        if page < 1:
            page = 1

        paginator = Paginator(data, 10)
        num_pages = paginator.num_pages

        if page > num_pages:
            page = num_pages

        pa = paginator.page(page)
        obj_list = pa.object_list
        count = pa.paginator.count

        previous_url = '{}?page={}'.format(path, page - 1)
        next_url = '{}?page={}'.format(path, page + 1)
        if page == 1:
            previous_url = None

        if page == num_pages:
            next_url = None

        response_data = {
            'results': obj_list,
            'next_url': next_url,
            'previous_url': previous_url,
            'count': count,
            'num_pages': num_pages,
            'page': pa.number
        }

        return response_data


class PassedSubjectViewSet(ViewSet):
    """
    管理员功能：审核通过课题
    """

    def list(self, request):
        query_set = Subject.objects.filter(review_result=1)
        ser = SubjectSerializer(instance=query_set, many=True)
        res = PendingSubjectViewSet.pagination(ser.data, request)

        return Response(res)


class SelectSubjectViewSet(ViewSet):
    """
    学生模块： 选择课题
    """

    def list(self, request):
        subject_name = request.query_params.get('subject_name', "")
        office = int(request.query_params.get('office', 0))
        questioner = request.query_params.get('questioner', "")

        q1 = Q()
        q2 = Q()
        q3 = Q()
        if subject_name:
            q1 = Q(subject_name__icontains=subject_name)

        if office:
            q2 = Q(office=office)

        if questioner:
            q3 = Q(questioner=questioner)

        query_set = Subject.objects.filter(q1, q2, q3, review_result=1)
        ser = SubjectSerializer(instance=query_set, many=True)
        res = PendingSubjectViewSet.pagination(ser.data, request)

        return Response(res)

    def update(self, request, pk=None):
        if not pk:
            return Response("请传入课题参数", status=400)

        user = request.user.student
        if hasattr(user, 'select_student'):
            return Response("你已经选择了课题!", status=400)
        if hasattr(user, 'apply_students'):
            return Response("你已经申请了课题,课题编号: {},请等待老师审核!".format(user.apply_students.id), status=400)

        sub = Subject.objects.filter(id=pk)
        if not sub.exists():
            return Response("该课题不存在!", status=400)

        sub = sub[0]
        if sub.select_student:
            return Response("该课题已经有人选择,请选择其他课题", status=400)
        if sub.apply_students:
            return Response("该课题已经有人申请,请申请其他课题", status=400)

        sub.apply_students = user
        sub.save()

        return Response("选题成功! 请等待老师审核.")




