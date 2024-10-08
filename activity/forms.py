from django import forms
from django.contrib.auth import authenticate
from django.forms import NumberInput, TextInput, PasswordInput, EmailInput
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
    
    def is_authenticated(self, username, password):
        try:
            user = User.objects.get(username=username)

            if user.username == username and user.password == password:
                return True
        except:
            print("Object does not exist")

    

class CreateAccount_ChangePasword_Form(forms.ModelForm):
    confirm_password = forms.CharField(widget=PasswordInput(attrs={"class":"form-control",
                                             "id":"change_password",
                                             "name":"change_password",
                                             "required": True,
                                             "placeholder": "Confirm password",}))
    class Meta:
        model = User
        fields = ["username","password", "name", "email"]
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

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password is not confirm_password:
    #         raise ValidationError("Password do not match")
        
    #     return cleaned_data


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
