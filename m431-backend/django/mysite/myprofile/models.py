from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)  # La liaison OneToOne vers le modele User

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
