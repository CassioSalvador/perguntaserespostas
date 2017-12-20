from django import forms
from django.forms import ModelForm
from .models import Quiz, FatherQuiz

class FatherQuizForm(ModelForm):
    class Meta:
        model = FatherQuiz
        fields = [
            'title'
        ]

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'question', 'right_option', 'first_option', 'second_option', 'third_option', 'fourth_option'
        ]

#class QuizForm(forms.Form):
#    title = forms.CharField(max_length=100)
#    question = forms.TextField(help_text="Insira sua pergunta")
#    right_option = forms.TextField(help_text="Escreva aqui a resposta correta para a pergunta")
#    first_option = forms.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
#    second_option = forms.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
#    third_option = forms.TextField(help_text="Insira aqui uma resposta alternativa (errada)")
#    fourth_option = forms.TextField(help_text="Insira aqui uma resposta alternativa (errada)")

        
