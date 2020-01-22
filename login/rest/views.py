from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class TestViewSet(ViewSet):
    """

    """
    def list(self, request):
        print(request.user)
        if hasattr(request.user, "teacher"):
            print("Teacher")
        return Response({"status": "OK"})
