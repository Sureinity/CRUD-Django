from .decorators import check_session_or_redirect, session_expiration_or_redirect
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import FruitForm, SearchForm, AuthenticationForm, CreateAccount_ChangePasword_Form
from .models import Fruits, User
# Create your views here.

#-----------------------------------#TODO: Work with "Session Management: ALMOST DONE"----------------------------------------------#
#TODO: @authenticated_or_login still need configuration. User can still redirect to login page with [ALT + <-]: DONE
#TODO: When user performs CRUD operations on expired session and logs in back, CRUD are still executed afterwards: NOT YET ADDRESSED

##########################################
#             AUTHENTICATION             #
##########################################

@never_cache # URL 'login' will never be cached; user will not be directed to that page if it using browser's navigation [ALT + left|right arrow keys]
@check_session_or_redirect
def login(request):
    request.session.flush() # *DEBUG* Flush sessions when directed to Login URL
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request.POST) # Populate form with value from request.POST
        if form.is_valid():
            username = form.cleaned_data["username"] # Fetch cleaned data/value from populated form
            password = form.cleaned_data["password"] #

            user = User.objects.get(username=username)
            if form.is_authenticated(username, password): # Method from forms.AuthenticationForm
                request.session["id"] = user.id     # These statements declare session data mapped with session ID (Found in database: django_session)
                request.session["role"] = user.role #
                messages.success(request, "Login Successful!") 
                return redirect("list_fruit")
        else:
            print(form.errors)
        
    return render(request,"login.html", {"form": form})

def logout(request):
    return redirect("list_fruit")

def create_account(request):
    form = CreateAccount_ChangePasword_Form()

    if request.method == "POST":
        form = CreateAccount_ChangePasword_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            print(username)
            print(password)
            return redirect("login")
        
    return render(request,"createAccount.html", {"form":form})

def change_password(request):
    form = CreateAccount_ChangePasword_Form()

    if request.method == "POST":
        form = CreateAccount_ChangePasword_Form(request.POST)

    context = {
        "form": form
    }
    return render(request, "changePassword.html", context)


##########################################
#               FRUITS CRUD              #
##########################################
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

def create_fruit(request):
    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            messages.success(request, "Fruit successfully created!")
            form.save()
            return redirect("list_fruit")
    else:
        form = FruitForm()
    
    #Database objects
    outputData = Fruits.objects.all()
    return redirect("list_fruit")

#----------------------------------------------------------

def delete_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruits, id=fruit_id)

    if request.method == "POST":
        fruit.delete()
        messages.success(request, "Fruit succesfully deleted!")
    else:
         messages.error(request, "Deletion error!")

    return redirect("list_fruit")

#----------------------------------------------------------

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
