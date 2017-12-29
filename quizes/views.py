from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

#Imports for the user management
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

# Import for the formset
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

# Imports for User creation
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import Quiz, FatherQuiz
from .forms import QuizForm, FatherQuizForm

# Create your views here.
def index(request):
    return render(request, "quizes/index.html")

# User registration
class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

# Quiz registration
class QuizRegister(View):
    
    def get(self, request, *args, **kwargs):
        submitted = False
        # Creating a new formset for displaying fields
        QuizFormSet = formset_factory(QuizForm, extra=5)
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
        return render(request, "quizes/quiz_registration.html", context)

    def post(self, request, *args, **kwargs):
        submitted = False
        # Creating a new modelformset for saving
        QuizFormSet = modelformset_factory(Quiz, fields=('question', 'right_option', 'first_option', 'second_option', 'third_option', 'fourth_option'), extra=3)
        # Creating a new FatherQuizForm
        fatherquizform_formclass = FatherQuizForm
        # Instanciating forms
        fatherquizform = fatherquizform_formclass(request.POST)
        formset = QuizFormSet(request.POST)
        # Validating forms and saving
        if formset.is_valid() & fatherquizform.is_valid():
            fatherQuiz = fatherquizform.save(commit=False)
            # Checking if the quiz was created by a specific user
            try:
                # If so, the quiz will be assigned to the user
                fatherQuiz.username = request.user
            except Exception:
                # If not, it will take the control back to the next line
                pass
            fatherQuiz.save()
            fatherQuiz.url = "http://" + request.get_host() + "/quiz/" + str(fatherQuiz.id)
            fatherQuiz.save()
            forms = formset.save(commit=False)
            for form in forms:
                form.fatherquiz = fatherQuiz
                form.save()
            submitted = True
            #return HttpResponseRedirect('/quiz_registration?submitted=True')
        context = {
            'fatherquizurl': fatherQuiz.url,
            'formset': formset, 
            'fatherquizform': fatherquizform,
            'submitted': submitted
        }
        return render(request, "quizes/quiz_registration.html", context)
            
class AnswerQuiz(View):
    
    def get(self, request, *args, **kwargs):
        fatherquiz = FatherQuiz.objects.get(id=kwargs['fquiz_id'])
        quizes = fatherquiz.quiz_set.all()
        context = {
            'fatherquiz': fatherquiz,
            'quizes': quizes
        }
        
        return render(request, "quizes/answer.html", context)

    def post(self, request, *args, **kwargs):
        return render(request, "quizes/answer.html")

    # Ver como pegar o id do quiz pai passado na url
    # Selecionar o model
    # Dar loop e exibir quiz filhos