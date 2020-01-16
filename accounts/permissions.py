from rest_framework import permissions

#custom owner permission specifying if the user is the owner of the object


class is_user(permissions.BasePermission):
    """
    Object-level permission to only allow user to edit user stuff
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # Instance must have an attribute named `owner`.
        return obj == request.user
