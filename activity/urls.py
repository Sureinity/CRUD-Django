from django.urls import path
from . import views

urlpatterns = [
    #Login
    path("", views.login, name="login"),
    path("createAccount/", views.create_account, name="create_account"),
    path("changePassword/", views., name="change_password"),


    #Fruits CRUD
    path("fruits/", views.list_search, name="list_fruit"),
    path("fruits/searchFruit/", views.list_search, name="search_query"),
    path("createFruit/", views.create_fruit, name="create_fruit"),
    path("deleteFruit/<int:fruit_id>/", views.delete_fruit, name="delete_fruit"),
    path("editFruit/<int:fruit_id>/", views.edit_fruit, name="edit_fruit"),
]
