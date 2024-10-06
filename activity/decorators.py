# from functools import wraps
from django.shortcuts import redirect

# def authenticated_or_login(view_func):
#     # @wraps(view_func)
#     def _wrapped_view(request):
#         if request.session.get("id"):  # Check if the user is logged in
#             return redirect("list_fruit")  # Redirect to the fruits page
#         return view_func(request)
        
#     return _wrapped_view

# def authenticated_or_login(func):
#     def wrapper(request):
#         if request.session.get("id"):
#             return redirect("list_fruit")
#         else:
#             return func(request)

#     return wrapper

def authenticated_or_login(view_func):
    def wrapper(request):
        if request.session.get("id"):
            return redirect("list_fruit")
        else:
            return view_func(request)
    return wrapper