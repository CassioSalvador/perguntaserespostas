from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    right_option = models.TextField()
    first_option = models.TextField()
    second_option = models.TextField()
    third_option = models.TextField()
    fourth_option = models.TextField()
    username = models.ForeignKey(User, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)