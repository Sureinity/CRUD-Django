# from functools import wraps
from django.shortcuts import redirect, render


def check_session_or_redirect(view_func):
    def wrapper(request):
        if request.session.get("id") and request.session["role"] == "2":
            return redirect("list_fruit")
        return view_func(request)
    return wrapper


#PROBLEM: Fix when there is no session or user is still not logged in, the session_expired.html should not be accessible/shown: NOT YET IMPLEMENTED
def session_expiration_or_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("id"):
            return redirect("login")
        elif request.session["role"] == "1":
            pass
        return view_func(request, *args, **kwargs)
    return wrapper
