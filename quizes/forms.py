from django import forms
from django.forms import ModelForm, CharField
from .models import Quiz, FatherQuiz

class FatherQuizForm(ModelForm):
    class Meta:
        model = FatherQuiz
        fields = [
            'title'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Defina o nome deste Quiz (ex: Meus Hobbies)"}),
        }

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'question', 'right_option', 'first_option', 'second_option', 'third_option', 'fourth_option'
        ]
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insira uma pergunta"}),
            'right_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insira a resposta correta para a pergunta"}),
            'first_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insira uma resposta incorreta"}),
            'second_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insira uma resposta incorreta"}),
            'third_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insira uma resposta incorreta"}),
            'fourth_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Insira uma resposta incorreta"}),
        }

        
