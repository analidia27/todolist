from django.contrib import admin
from todoListApp.models import ToDoList, ToDoItem, Category,State

admin.site.register(ToDoList)
admin.site.register(ToDoItem)
admin.site.register(Category)

admin.site.register(State)

