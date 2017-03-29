from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerorObjectReadOnly(BasePermission):
    msg='you must be the owner of this object'
    my_safe_methods = [ 'GET', 'PUT', 'CREATE']
    # def has_permission(self, request, view):
    #     if request.method in self.my_safe_methods:
    #         # return obj.user == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in self.my_safe_methods:
            return obj.user == request.user