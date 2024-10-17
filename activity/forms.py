from django import forms
from django.contrib.auth import authenticate
from django.forms import NumberInput, TextInput, PasswordInput, EmailInput, IntegerField
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from .models import User, Fruits

##########################################
#             AUTHENTICATION             #
##########################################
class AuthenticationForm(forms.Form):
    username =  forms.CharField(widget=TextInput(attrs={"class":"form-control",
                                             "id":"username",
                                             "name":"username",
                                             "required": True,}))
    password =  forms.CharField(widget=PasswordInput(attrs={"class":"form-control",
                                             "id":"password",
                                             "name":"password",
                                             "required": True,}))
    
    def authenticate(self, username, password):
        user = User.objects.get(username=username)
        if user.username == username and check_password(password, user.password):
            return True

    

class EditAccount_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
                "username": TextInput(attrs={"class":"form-control",
                                             "id":"username",
                                             "name":"username",
                                             "required": True,
                                             "placeholder": "Enter username",}),
                "password": PasswordInput(attrs={"class":"form-control",
                                             "id":"password",
                                             "name":"password",
                                             "required": True,
                                             "placeholder": "Enter password",}),
                "name": TextInput(attrs={"class":"form-control",
                                             "id":"name",
                                             "name":"name",
                                             "required": True,
                                             "placeholder": "Enter name",}),
                "email": EmailInput(attrs={"class":"form-control",
                                             "id":"email",
                                             "name":"email",
                                             "required": True,
                                             "placeholder": "Enter username",}),
        }

class CreateAccount_Form(EditAccount_Form):
    confirm_password = forms.CharField(widget=PasswordInput(attrs={"class":"form-control",
                                             "id":"confirm_password",
                                             "name":"confirm_password",
                                             "required": True,
                                             "placeholder": "Confirm password",}))
    


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruits
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
