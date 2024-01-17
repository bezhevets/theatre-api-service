from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoObjectPermissions


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class AnonReadOnly(DjangoObjectPermissions):
    authenticated_users_only = False
