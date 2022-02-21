from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    description = models.CharField(max_length=200,
                                   help_text='Task description')
    time = models.DateTimeField(null=True,
                                blank=True,
                                help_text='Task date and time')
    is_completed = models.BooleanField(default=False,
                                       help_text='Task is completed?')

