from rest_framework.permissions import BasePermission


class ProjectImportPermission(BasePermission):
    """
    Checks if the user has access to the project import API
    Default case is always true
    """

    def has_permission(self, request, view):
        return True


class IsProjectMember(BasePermission):
    """Allow access only to project members or organization admins."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_organization_admin(obj.organization_id):
            return True
        return obj.members.filter(user=request.user, enabled=True).exists()
