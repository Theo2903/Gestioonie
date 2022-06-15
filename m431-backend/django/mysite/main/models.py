from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appreciation(models.Model):
    date_time = models.DateTimeField()
    appreciation = models.ForeignKey('Observation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Observation(models.Model):
    title = models.CharField(max_length=255)
    key = models.CharField(max_length=3)

