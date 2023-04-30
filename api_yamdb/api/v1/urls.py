from api.v1.views import (CategoryViewSet, CommentViewSet, GenresViewSet,
                          ReviewViewSet, TitelsViewSet, UsersViewSet,
                          sign_up_confirmation_view, sign_up_view)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenresViewSet)
router.register('titles', TitelsViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
auth_urls = [
    path('signup/', sign_up_view, name='signup'),
    path('token/', sign_up_confirmation_view, name='token'),
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', include(router.urls)),
]
