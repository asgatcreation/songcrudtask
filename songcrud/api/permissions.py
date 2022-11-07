from rest_framework import permissions

class IsCratorOrAdminReadOnly(permissions. BasePermssion):
    def has_object_permssion(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_artisteuser and request.method not in self.edit_methods:
            return True
        
        if request.user.is_superuser:
            return True
        
        if request.user ==obj:
            return True