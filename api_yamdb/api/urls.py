from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet, UserCreateViewSet,
    UserReceiveTokenViewSet, UserViewSet
)

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)

auth_urls = [
    path(
        'signup/',
        UserCreateViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        'token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    )
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(auth_urls)),
]
