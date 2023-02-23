from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentsViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, create,
                    get_token)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet, basename='comments'
)
router.register('users', UserViewSet, basename='users')

urlpatterns_auth = [
    path('signup/', create, name='register_user'),
    path('token/', get_token, name='token'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(urlpatterns_auth)),
]
