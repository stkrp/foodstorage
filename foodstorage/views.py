from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.reverse import reverse


class IndexAPI(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        urls = [
            reverse(name, request=request) for name in (
                'auth', 'user-list', 'photo-list', 'rating-list',
            )
        ]
        return Response(urls)
