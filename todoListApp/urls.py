from django.urls import path
from . import views


urlpatterns = [
    path("", views.ToDoList_LV.as_view(), name="index"),
    path("new",views.list_create,name='list_create'),
    path("update/<int:pk>/",views.list_update,name='list_update'),
    path("delete/<int:pk>/",views.list_delete,name='list_delete'),
    
    path("<int:list_id>/", views.todo_item_list, name="list"), 
    path("<int:list_id>/item/new",views.item_create,name='item_create'),
    path("item/update/<int:pk>/",views.item_update,name='item_update'),
    path("item/delete/<int:pk>/",views.item_delete,name='item_delete'),
    
    #path("<int:list_id>/item/new",views.item_create,name='item_create'),
    #path("<int:list_id>/item/update/<int:pk>/",views.item_update,name='item_update'),
    #path("<int:list_id>/item/delete/<int:pk>/",views.item_delete,name='item_delete'),



]
