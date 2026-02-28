from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostsViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('generic-view/', PostsGenericViewGET.as_view()),
    path('generic-view-post/', PostsGenericView.as_view()),
    path('generic-view/update/<int:pk>/', PostsUpdateGenericView.as_view()),
    path('generic-view/delete/<int:pk>/', PostsDeleteGenericView.as_view()),
]