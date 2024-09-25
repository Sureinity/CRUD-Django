from django.shortcuts import render, redirect
from .forms import CreateForm
from .models import Fruits
# Create your views here.


def list_fruit(request):
    fruits = Fruits.objects.all()
    form = CreateForm()

    context = {
        "form": form,
        "output": fruits,
    }
    
    return render(request, "index.html", context)



def create_fruit(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_fruit")
    else:
        form = CreateForm()
    
    #Database objects
    outputData = Fruits.objects.all()
    context = {
        "form" : form,
    }
    return redirect("list_fruit")

def delete_fruit(request, pk):
    if request.method == "POST":
        objectDelete = Fruits.objects.get(id=pk)
        print(objectDelete)
        #delete = objectDelete.delete()
    
    data = Fruits.objects.all()
    context = {
        "object": data
    }
