from django.db import models
from django.contrib.auth.models import User
# Imports to link UserProfile to User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class FatherQuiz(models.Model):
    title = models.CharField("Nome do Quiz", max_length=100)
    username = models.ForeignKey(User, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Quiz(models.Model):
    question = models.TextField("Pergunta")
    right_option = models.TextField("Resposta Correta")
    first_option = models.TextField("Resposta Incorreta nº1")
    second_option = models.TextField("Resposta Incorreta nº2")
    third_option = models.TextField("Resposta Incorreta nº3")
    fourth_option = models.TextField("Resposta Incorreta nº4")
    # One-to-many relationship between a FatherQuiz and Quizes (child quiz)
    fatherquiz = models.ForeignKey(FatherQuiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class UserProfile(models.Model):
    GENDER_CHOICES = ( 
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE) # Includes: {first_name, last_name, email}-blank=True - groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
    profile_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    gender = models.CharField(max_length=40, blank=True, null=True, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=300, blank=True, null=True)
    city = models.TextField(max_length=50, blank=True, null=True)
    country = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)