from rest_framework.generics import ListCreateAPIView

from .models import User
from .serializers import UserSerializer


class Users(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
