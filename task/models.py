from django.db import models
from django.contrib.auth.models import User # <-- import User

class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)# <-- link to user

    def __str__(self):
        return self.title
