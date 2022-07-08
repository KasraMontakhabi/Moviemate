# Custom permission

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:  # safe methods are: GET ,HEAD ,OPTIONS
            return True
        else:
            return bool(request.user and request.user.is_staff)
            # request.user is the logged in user (Showing in up right corner of the page)
            # checking if the user that sends a request rather than GET, is the admin or not. If he is, then has permission


class IsReviewUserOrReadOnly(permissions.BasePermission):

    # check if the user has permission to edit the object (for example a single review)
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # safe methods are: GET ,HEAD ,OPTIONS
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff
            # checking if the user that sends a request rather than GET, is the user that wrote the review or not. If he is, then has permission
