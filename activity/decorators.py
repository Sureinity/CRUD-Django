from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render


def check_session_or_redirect(view_func):
    def wrapper(request):
        if request.session.get("id"):
            return redirect("list_fruit")
        return view_func(request)
    return wrapper


#PROBLEM: Fix when there is no session or user is still not logged in, the session_expired.html should not be accessible/shown: NOT YET IMPLEMENTED
def session_expiration_or_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            expiry_time_str = request.session.get("expiry_time")
            expiry_time = datetime.fromisoformat(expiry_time_str)
            if timezone.now() > expiry_time:
                messages.info(request, "Your session expired. Please log in again.")
                return render(request, "session_expired.html")
        except TypeError:
                return redirect("login")
        return view_func(request, *args, **kwargs)
    return wrapper

def only_admin(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get("role") == 2:
            return render(request, "not_authorized.html")
        return view_func(request, *args, **kwargs)
    return wrapper
