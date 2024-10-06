# from functools import wraps
from django.shortcuts import redirect, render

def check_session_or_redirect(view_func):
    def wrapper(request):
        if request.session.get("id"):
            return redirect("list_fruit")
        return view_func(request)
    return wrapper

def session_expiration_or_redirect(view_func):
    def wrapper(request):
        if not request.session.get("id"):
            # Delete or flush the request.POST before it goes to session_expired.html: NOT YET IMPLEMENTED
            return render(request, "session_expired.html")
        return view_func(request)
    return wrapper