from django import forms
from django.forms import ModelForm
from .models import Quiz

class QuizForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Quiz
        fields = [
            'question', 'right_option', 'first_option', 'second_option', 'third_option', 'fourth_option'
        ]
