from django.db import models
from django.contrib.auth.models import User

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

