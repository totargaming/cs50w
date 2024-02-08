from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField()
    complete = models.BooleanField(default=False)