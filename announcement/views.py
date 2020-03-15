from django.shortcuts import render
from django.views import View
# Create your views here.


class AnnouncementView(View):
    """
    公告视图
    """
    def get(self, request):
        return render(request, 'announcement.html')


