from django.db import models

from user.models import User

class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    detail = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('updated_at',)
