import random
from django.utils import timezone
from datetime import timedelta, datetime

from django.db.models import F
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password


from .decorators import check_session_or_redirect, session_expiration_or_redirect, only_admin
from .forms import FruitForm, SearchForm, AuthenticationForm, CreateAccount_Form, EditAccount_Form
from .models import Fruits, User
# Create your views here.

#-----------------------------------#TODO: Work with "Session Management: ALMOST DONE"----------------------------------------------#
#TODO: @authenticated_or_login still need configuration. User can still redirect to login page with [ALT + <-]: DONE
#TODO: When user performs CRUD operations on expired session and logs in back, CRUD are still executed afterwards: DONE
#TODO: Work with admin and logout
#TODO: Handling incorrect username or password 

#ADMIN CREATE ACCOUNT shell: User.objects.insert(username="admin", name="admin", email="", password="qwe", role="1") 

##########################################
#             AUTHENTICATION             #
##########################################

@never_cache # URL 'login' will never be cached; user will not be directed to that page if it using browser's navigation [ALT + left|right arrow keys]
@check_session_or_redirect
def login(request):
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                form.add_error(None, "Username or password incorrect.")  # Add error to the form
                return render(request, "login.html", {"form": form })

            if check_password(password, user.password):
                print("correct")
            else:
                print("wrong")

            if form.authenticate(username, password):
                request.session["username"] = user.username 
                request.session["id"] = user.id
                request.session["role"] = user.role
                
                expiry_time = timezone.now() + timedelta(seconds=request.session.get_expiry_age())
                request.session["expiry_time"] = expiry_time.isoformat()
                
                if request.session["role"] == 1:
                    return redirect("admin")
                
                welcomeMessages = [
                    f"Hello there, {user.name}!",
                    f"Good evening, {user.name}!"
                ]
                messages.success(request, random.choice(welcomeMessages))
                return redirect("list_fruit")
            else:
                form.add_error(None, "Username or password incorrect.")  # Add error if authentication fails
                return render(request, "login.html", {"form": form})
    
    return render(request, "login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        request.session.flush()
    
    return redirect("login")

@never_cache
def session_expired(request):
    return render(request, "session_expired.html")



##########################################
#               FRUITS CRUD              #
##########################################
@never_cache
@session_expiration_or_redirect
def list_search(request): 
    
    fruitForm = FruitForm()
    searchForm = SearchForm()
    
    #List Fruits
    fruits = Fruits.objects.all()
    
    #Search function
    if request.method == "GET":
        searchForm = SearchForm(request.GET)
        if searchForm.is_valid():
            query = searchForm.cleaned_data["query"]
            fruits = Fruits.objects.filter(fruit_name__icontains=query)
    
    context = {
        "searchForm": searchForm,
        "output": fruits,
        "form": fruitForm,
    }
    return render(request, "index.html", context)

#----------------------------------------------------------
@session_expiration_or_redirect
def create_fruit(request):
    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            fruit_name = form.cleaned_data['fruit_name']  
            quantity = form.cleaned_data['fruit_qty']  

            existing_fruit = Fruits.objects.filter(fruit_name=fruit_name).first() # Check if a fruit with the same name already exists
            if existing_fruit: # This is an object returned from the filter query
                existing_fruit.fruit_qty = F('fruit_qty') + quantity  # Use F expressions to avoid race conditions
                existing_fruit.save()
                messages.success(request, f"{quantity} added to existing fruit: {fruit_name}!")
            else:
                # If fruit does not exist, save the new fruit
                form.save()
                messages.success(request, "Fruit successfully created!")
            
            return redirect("list_fruit")
    else:
        form = FruitForm()

    return render(request, "create_fruit.html", {"form": form})

#----------------------------------------------------------
@session_expiration_or_redirect
def delete_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruits, id=fruit_id)

    if request.method == "POST":
        fruit.delete()
        messages.success(request, "Fruit succesfully deleted!")
    else:
         messages.error(request, "Deletion error!")

    return redirect("list_fruit")

#----------------------------------------------------------
@session_expiration_or_redirect
def edit_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruits, id=fruit_id)

    if request.method == "POST":
        form = FruitForm(request.POST, instance=fruit)
        if form.is_valid():
            messages.success(request, "Fruit successfully updated!")
            form.save()
    else:
        messages.error(request, "Update error!")
    
    return redirect('list_fruit')

##########################################
#                 ADMIN                  #
##########################################
@never_cache
@only_admin
@session_expiration_or_redirect
def admin(request):
    form = CreateAccount_Form()

    if request.method == "POST":
        form = CreateAccount_Form(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "userList": User.objects.exclude(id=1),
        "form": form,
    }

    return render(request, "admin.html", context)

@session_expiration_or_redirect
def create_account(request):
    if request.method == "POST":
        form = CreateAccount_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin")
    else:
        form = form = CreateAccount_ChangePasword_Form()

    print(form.errors)
    return render(request, "admin.html", {
        "userList": User.objects.all(),
        "form": form,  # Ensure form is passed back
    })

@session_expiration_or_redirect
def edit_account(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = EditAccount_Form(request.POST, instance=user)
        if form.is_valid():
            messages.success(request, "User successfully updated!")
            form.save()
    else:
        messages.error(request, "Update error!")
    print(form.errors)    
    return redirect('admin')

@session_expiration_or_redirect
def delete_account(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()

    return redirect("admin")
