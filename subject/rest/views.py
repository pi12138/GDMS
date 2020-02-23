from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.core.paginator import Paginator

from subject.models import Subject
from .serializers import SubjectSerializer


class PendingSubjectView(ListAPIView):
    """
    待审批课题
    """

    def get(self, request):
        page = request.query_params.get('page', 1)
        page = int(page)

        query_set = Subject.objects.filter(review_result=0)
        pagi = Paginator(query_set, 10)

        if page > pagi.num_pages:
            page = pagi.num_pages

        pa = pagi.page(page)
        obj_list = pa.object_list

        ser = SubjectSerializer(instance=obj_list, many=True)

        return Response(ser.data)
