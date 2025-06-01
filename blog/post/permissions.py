from rest_framework.permissions import BasePermission


class isAbove18(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if   int(user.age) < 18:
            self.message = 'You cant post. Age must be 18 or above.'
            return False
        return True