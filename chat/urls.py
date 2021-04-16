from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register('messages/page/<int:page>', views.MessageViewSet)

urlpatterns = [
    # path("api/v1/messages/page/<int:page>", views.MessageViewSet),
    path('api/v1/', include(router.urls)),
]