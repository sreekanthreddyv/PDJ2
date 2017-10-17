from django.db import models

# Create your models here.
class Hello(models.Model):
	person = models.TextField(max_length = 20)

	def __str__(self):
		return self.person
