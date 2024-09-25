from django.urls import path
from . import views

urlpatterns = [
    path("fruits/", views.list_fruit, name="list_fruit"),
    path("createFruit/", views.create_fruit, name="create_fruit"),
 #   path("created/", views.index),
]
