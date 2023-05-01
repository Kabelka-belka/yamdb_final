from rest_framework import permissions


class IsAdminOrSuperPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_staff or request.user.is_admin)
        )


class IsAdminOrAlloWGetOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method == 'GET'
            or request.user.is_authenticated
            and (request.user.is_staff or request.user.is_admin)
        )


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        )