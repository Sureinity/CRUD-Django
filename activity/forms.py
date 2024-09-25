from django import forms
from django.forms import NumberInput, TextInput
from . import models

class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Fruits
        fields = "__all__"
        widgets = {
                "fruit_name": TextInput(attrs={"class": "form-control", "name": "fruitName", "id":"fruitName", "required": True}),
                "fruit_qty": NumberInput(attrs={"class": "form-control", "name": "fruitQty", "id":"fruitQty", "required": True}),
        }
