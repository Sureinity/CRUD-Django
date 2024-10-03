from django import forms
from django.forms import NumberInput, TextInput, PasswordInput
from . import models

class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["username","password"]
        widgets = {
                "username": TextInput(attrs={"class":"form-control",
                                             "id":"username",
                                             "name":"username",
                                             "required": True,}),
                "password": PasswordInput(attrs={"class":"form-control",
                                             "id":"password",
                                             "name":"password",
                                             "required": True,}),
        }





class FruitForm(forms.ModelForm):
    class Meta:
        model = models.Fruits
        fields = "__all__"
        widgets = {
                "fruit_name": TextInput(attrs={"class": "form-control",
                                                "name": "fruitName",
                                                "id":"fruitName", 
                                                "required": True, 
                                                "autocomplete":False}),
                "fruit_qty": NumberInput(attrs={"class": "form-control",
                                                "name": "fruitQty",
                                                "id":"fruitQty",
                                                "required":True,
                                                "autocomplete":False}),
        }

class SearchForm(forms.Form):
   query = forms.CharField(required=False, widget=TextInput(attrs={"class":"form-control",
                                                                    "name":"fruitSearch",
                                                                    "id":"fruitSearch",
                                                                    "placeholder":"Search here...",
                                                                    "autofocus":False,
                                                                    "autocomplete": False}))
