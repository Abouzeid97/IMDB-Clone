from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            #check for read request
            return True
        else:
            #check for write request
            return bool(request.user and request.user.is_staff)
    
class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #check for read request
            return True
        else:
            #check for write request
            return obj.review_user == request.user
