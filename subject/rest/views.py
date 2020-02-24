from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.core.paginator import Paginator

from subject.models import Subject
from .serializers import SubjectSerializer


class PendingSubjectViewSet(ViewSet):
    """
    待审批课题
    """

    # def list(self, request):
    #     page = request.query_params.get('page', 1)
    #     page = int(page)
    #
    #     query_set = Subject.objects.filter(review_result=0).order_by('-declare_time')
    #     pagi = Paginator(query_set, 10)
    #
    #     if page > pagi.num_pages:
    #         page = pagi.num_pages
    #
    #     pa = pagi.page(page)
    #     obj_list = pa.object_list
    #
    #     ser = SubjectSerializer(instance=obj_list, many=True)
    #     data = {
    #         'result': ser.data,
    #         'next_url': "",
    #         'previous_url': "",
    #         'count': pa.count
    #     }
    #
    #     return Response(ser.data)

    def list(self, request):

        query_set = Subject.objects.filter(review_result=0).order_by('-declare_time')
        ser = SubjectSerializer(instance=query_set, many=True)
        res = self.pagination(ser.data, request)

        return Response(res)

    def pagination(self, data, request):
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
