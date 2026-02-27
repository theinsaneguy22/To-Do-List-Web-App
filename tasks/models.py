from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=now)

    def __str__(self):
        return self.title