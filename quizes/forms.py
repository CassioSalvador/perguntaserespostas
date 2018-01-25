from django import forms
from django.forms import ModelForm, CharField
from django.contrib.auth.models import User
from .models import Quiz, FatherQuiz, UserProfile
from django.core.files.images import get_image_dimensions

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

class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'id', 'first_name', 'last_name', 'email', 'last_login', 'date_joined'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'id': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu email. Ex: seuemail@gmail.com'}),
            'last_login': forms.DateInput(attrs={'class': 'form-control-plaintext rdonly', 'readonly': 'readonly'}),
            'date_joined': forms.DateInput(attrs={'class': 'form-control-plaintext rdonly', 'readonly': 'readonly'}),
        }
    # Removing requirement for fields
    #def __init__(self, *args, **kwargs):
    #        super(CustomUserForm, self).__init__(*args, **kwargs)
    #        for key in self.fields:
    #            self.fields[key].required = False

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_image', 'gender', 'birthday', 'address', 'city', 'country'
        ]
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': ''}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira seu endereço completo'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira sua cidade. Ex: Recife-PE'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o país em que vive'}),
        }
    
    

