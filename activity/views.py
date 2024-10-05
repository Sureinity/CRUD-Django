from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import FruitForm, SearchForm, AuthenticationForm, CreateAccount_ChangePasword_Form
from .models import Fruits, User
# Create your views here.

#-----------------------------------#TODO: Work with "Login Account view"----------------------------------------------#

##########################################
#             AUTHENTICATION             #
##########################################
def login(request):
    request.session.flush()
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.get(username=username)
            if user.password == password:
                request.session["id"] = user.id
                request.session["role"] = user.role
                print(request.session["role"])
                messages.success(request, "Login Successful!")  
                return redirect("list_fruit")
        else:
            print(form.errors)
        
    return render(request,"login.html", {"form": form})

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

def list_search(request):
    #Forms to render on initial load
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
