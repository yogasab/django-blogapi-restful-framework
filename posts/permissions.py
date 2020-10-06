from rest_framework import permissions

# class BasePermission(object):
#     # A base class from which all permisions classes should inherit
#     def has_permissions(self, request, view):
#         # Return True if permissions is granted, 'False' otherwise
#         return True

#     def has_object_permission(self, request, view, obj):
#         # Return True if permissions is granted, 'False' otherwise
#         return True

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj,):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user