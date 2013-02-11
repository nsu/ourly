from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WorkSession(models.Model):
    user = models.ForeignKey(User)
    start = models.DateTimeField()
    stop = models.DateTimeField(blank=True, null=True)

