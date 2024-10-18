from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render


def check_session_or_redirect(view_func):
    def wrapper(request):
        if request.session.get("role") == 2:
            return redirect("list_fruit")
        if request.session.get("role") == 1:
            return redirect("admin")
        return view_func(request)
    return wrapper


def session_expiration_or_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            expiry_time_str = request.session.get("expiry_time")
            expiry_time = datetime.fromisoformat(expiry_time_str)
            if timezone.now() > expiry_time:
                messages.info(request, "Your session expired. Please log in again.")
                return redirect("login")
        except TypeError:
                messages.info(request, "Your session expired. Please log in again.")
                return redirect("login")
        return view_func(request, *args, **kwargs)
    return wrapper

def only_admin(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get("role") == 2:
            return render(request, "not_authorized.html")
        return view_func(request, *args, **kwargs)
    return wrapper
