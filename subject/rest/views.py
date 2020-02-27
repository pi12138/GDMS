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



