from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import FruitForm, SearchForm, AuthenticationForm
from .models import Fruits, User

import datetime
# Create your views here.

#-----------------------------------#TODO: Work with "Create Account view"----------------------------------------------#

##########################################
#             AUTHENTICATION             #
##########################################
def login(request):
    form = AuthenticationForm()
    context = {
        "form":form,
    }
    return render(request,"login.html", context)

def create_account(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(username=username, password=password, role="user")
            form.save()
            print(username)
            print(password)
            print(user)
            return redirect("login")
        
    return render(request,"createAccount.html")


def change_password(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request.method)

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
    message = "Fruit Created!"
    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid:
            messages.success(request, "Fruit successfully created!")
            form.save()

      #TODO: Perform basic arithmetic when existing fruit name is created.

      # name = request.POST.get("fruit_name")
      #  quantity = int(request.POST.get("fruit_qty"))

      #  fruitName, created = Fruits.objects.get_or_create(fruit_name=name)

      #  if form.is_valid():
      #      if not created:
      #          fruitName.quantity += quantity
      #          form.save()
      #      else:
      #          fruitName.quantity = quantity
      #          form.save()

            return redirect("list_fruit")
    else:
        form = CreateForm()
    
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
