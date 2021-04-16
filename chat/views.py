from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import viewsets

from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-creation_date')
    serializer_class = MessageSerializer


schema_view = get_schema_view(
    openapi.Info(
        title = "Snippets API",
        default_version = 'v1',
        description = "Test description",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email = "contact@snippets.local"),
        license = openapi.License(name = "BSD License"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)
