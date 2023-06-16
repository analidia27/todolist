from django.db import models
from django.utils import timezone
from django.urls import reverse


def one_week_hence():
	return timezone.now() + timezone.timedelta(days=7)


class Category(models.Model):
	title = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return self.title

class State(models.Model):
	name = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return self.name 

class ToDoList(models.Model):
	title = models.CharField(max_length=100, unique=True)
	
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	
	#created_date = models.DateTimeField(auto_now_add=True)
	created_date = models.DateTimeField(default=timezone.now())
	due_date = models.DateTimeField(default=one_week_hence)
	state = models.ForeignKey(State,on_delete=models.CASCADE)

	def get_absolute_url(self):
		#return reverse("list", args[self.id])
		return reverse("list", [self.id])

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["due_date"]


class ToDoItem(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)


	def get_absolute_url(self):
		return reverse (
			"item-update", args=[str(self.ToDoList.id), str(self.id)]
		)


	def __str__(self):
		return f"{self.title}"



