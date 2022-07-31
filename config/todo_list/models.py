from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['completed']
    
    def __str__(self):
        return self.title
    
    