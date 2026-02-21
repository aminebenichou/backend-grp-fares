from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()

router.register("Users", UsersViewSet)
router.register("groups", GroupsViewSet)
router.register('perms', PermissionsViewSet)



urlpatterns=[
    path('', include(router.urls))
]