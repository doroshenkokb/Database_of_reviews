from rest_framework import permissions


class IsSuperUserOrIsAdminOnly(permissions.BasePermission):
    """
    Права для суперюзера, админа или
    аутентифицированного пользователя с ролью admin.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_staff
                 or request.user.is_admin)
        )


class AnonimReadOnly(permissions.BasePermission):
    """Безопасны запросы для анонимного юзера."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsSuperUserIsAdminIsModeratorIsAuthor(permissions.BasePermission):
    """
    Безопасны запросы для анонимного юзера.
    Запросы PATCH и DELETE только для
    суперпюзера, админа, аутентифицированного пользователя
    с ролью admin или moderator, а также автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_staff
                 or request.user.is_admin
                 or request.user.is_moderator
                 or request.user == obj.author)
        )
