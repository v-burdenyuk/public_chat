from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', views.schema_view.without_ui(cache_timeout = 0), name = 'schema-json'),
    re_path(r'^swagger/$', views.schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
    re_path(r'^redoc/$', views.schema_view.with_ui('redoc', cache_timeout = 0), name = 'schema-redoc'),
]
