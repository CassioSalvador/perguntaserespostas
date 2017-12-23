from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

#Imports for the user management
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

#Import for the formset
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

from .models import Quiz, FatherQuiz
from .forms import QuizForm, FatherQuizForm

# Create your views here.
def index(request):
    return render(request, "quizes/index.html")

class QuizRegister(View):
    
    def get(self, request, *args, **kwargs):
        submitted = False
        # Creating a new formset for displaying fields
        QuizFormSet = formset_factory(QuizForm, extra=3)
        # Creating a new FatherQuizForm
        fatherquizform_formclass = FatherQuizForm
        # Defining initial values for the instances
        initial = {'key': 'value'}
        # Instanciating forms
        formset = QuizFormSet()
        fatherquizform = fatherquizform_formclass(initial=initial)
        if 'submitted' in request.GET:
            submitted = True
        context = {
        'formset': formset, 
        'fatherquizform': fatherquizform,
        'submitted': submitted
        }
        return render(request, "quizes/register.html", context)

    def post(self, request, *args, **kwargs):
        submitted = False
        # Creating a new modelformset for saving
        QuizFormSet = modelformset_factory(Quiz, fields=('question', 'right_option', 'first_option', 'second_option', 'third_option', 'fourth_option'), extra=3)
        # Creating a new FatherQuizForm
        fatherquizform_formclass = FatherQuizForm
        # Instanciating forms
        fatherquizform = fatherquizform_formclass(request.POST)
        formset = QuizFormSet(request.POST)
        # Validating forms
        if formset.is_valid() & fatherquizform.is_valid():
            fatherQuiz = fatherquizform.save(commit=False)
            fatherQuiz.save()
            fatherQuiz.url = "http://127.0.0.1:8000/quiz/" + str(fatherQuiz.id)
            fatherQuiz.save()
            forms = formset.save(commit=False)
            for form in forms:
                form.fatherquiz = fatherQuiz
                form.save()
            return HttpResponseRedirect('/register?submitted=True')
        context = {
        'formset': formset, 
        'fatherquizform': fatherquizform,
        'submitted': submitted
        }
        return render(request, "quizes/register.html", context)
            
#class AnswerQuiz(View):
#    form_class = QuizForm

