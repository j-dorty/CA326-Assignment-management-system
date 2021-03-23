from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.user_type in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator


            