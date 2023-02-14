from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=200,null=True,blank=True)
    is_completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.task}'