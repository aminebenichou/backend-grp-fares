from rest_framework import permissions

from django.contrib.auth.models import Permission, Group


class isGmailUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and '@gmail.com' in request.user.email:
            return True
        return False
    

class canAddPost(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='addpostgroup').exists()