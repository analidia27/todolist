from .models import *
from django import forms
from django.forms.widgets import NumberInput

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title','category','created_date','due_date','state')
        widgets = {
        'created_date': NumberInput(attrs={'type': 'date'}),
        'due_date': NumberInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Titulo',
            'category': 'Categoria',
            'created_date': 'Fecha creado',
            'due_date': 'Fecha vencimiento',
            'state': 'Estado'
        }
        
class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('title','description','todoList')   
        labels = {
            'title': 'Titulo',
            'description': 'Descripción',

        }





