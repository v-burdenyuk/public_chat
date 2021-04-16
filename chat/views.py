from rest_framework import viewsets
# from rest_framework.pagination import LimitOffsetPagination

from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-creation_date')
    serializer_class = MessageSerializer
    # pagination_class = LimitOffsetPagination