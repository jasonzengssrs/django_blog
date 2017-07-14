from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = name = models.CharField(max_length=70)
	
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()
	excerpt = models.CharField(max_length=200, blank=True)

	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()


	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})

	
