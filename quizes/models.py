from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FatherQuiz(models.Model):
    title = models.CharField(max_length=100)
    username = models.ForeignKey(User, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Quiz(models.Model):
    question = models.TextField(help_text="Insira sua pergunta")
    right_option = models.TextField(help_text="Escreva aqui a resposta correta para a pergunta")
    first_option = models.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
    second_option = models.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
    third_option = models.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
    fourth_option = models.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
    # One-to-many relationship between a FatherQuiz and Quizes (child quiz)
    fatherquiz = models.ForeignKey(FatherQuiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

