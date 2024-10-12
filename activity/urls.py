from django.urls import path
from . import views

urlpatterns = [
    #Authentication System
    path("", views.login, name="login"),
    path("changePassword/", views.change_password, name="change_password"),
    path("logout/", views.logout, name="logout"),

    # Admin
    path("admin/", views.admin, name="admin"),
    path("admin/createAccount/", views.create_account, name="create_account"),
    path("admin/editAccount/<int:user_id>", views.edit_account, name="edit_account"),
    path("admin/deleteAccount/<int:user_id>", views.delete_account, name="delete_account"),

    #Fruits CRUD
    path("fruits/", views.list_search, name="list_fruit"),
    path("fruits/searchFruit/", views.list_search, name="search_query"),
    path("createFruit/", views.create_fruit, name="create_fruit"),
    path("deleteFruit/<int:fruit_id>/", views.delete_fruit, name="delete_fruit"),
    path("editFruit/<int:fruit_id>/", views.edit_fruit, name="edit_fruit"),
]
