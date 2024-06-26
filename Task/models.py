from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    deadline=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.name
