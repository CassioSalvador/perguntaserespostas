from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse

#Imports for the user management
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

# Import for the formset
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

# Imports for User creation
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Imports for Quiz listing
from django.views.generic import ListView

from .models import Quiz, FatherQuiz
from .forms import QuizForm, FatherQuizForm

# Create your views here.
def index(request):
    return render(request, "quizes/index.html")

class FatherQuizList(ListView):
    model = FatherQuiz
    context_object_name = 'fatherquizes'

    def get_queryset(self):
        return FatherQuiz.objects.all()

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
        QuizFormSet = modelformset_factory(Quiz, fields=('question', 'right_option', 'first_option', 'second_option', 'third_option', 'fourth_option'), extra=5)
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

# Quiz answering            
class AnswerQuiz(View):

    def get(self, request, *args, **kwargs):
        submitted = False
        # Selecting FatherQuiz from the route
        fatherquiz = FatherQuiz.objects.get(id=kwargs['fquiz_id'])
        # Selecting all quizes related to FatherQuiz
        quizes = fatherquiz.quiz_set.all()
        items = []
        for quiz in quizes:
            items.append([quiz.right_option, quiz.first_option, quiz.second_option, quiz.third_option, quiz.fourth_option])
        if 'submitted' in request.GET:
            submitted = True
        context = {
            'fatherQuiz': fatherquiz,
            'quizes': quizes,
            'items': items,
            'submitted': submitted
        }
        
        return render(request, "quizes/answer.html", context)

    def post(self, request, *args, **kwargs):
        submitted = False
        # Selecting FatherQuiz from the route
        fatherquiz = FatherQuiz.objects.get(id=kwargs['fquiz_id'])
        # Selecting all quizes related to FatherQuiz
        quizes = fatherquiz.quiz_set.all()
        answers = request.POST
        items = []
        allanswers = []
        score = 0
        for quiz in quizes:
            items.append([quiz.right_option, quiz.first_option, quiz.second_option, quiz.third_option, quiz.fourth_option])
            answer = answers.get('option-'+str(quiz.id))
            if quiz.right_option == answer:
                score += 1
            else:
                pass
            allanswers.append(answer)
        submitted = True
        listing = zip(quizes,allanswers)
        context = {
            'fatherQuiz': fatherquiz,
            'quizes': quizes,
            'items': items,
            'submitted': submitted,
            'score': score,
            'allanswers': allanswers,
            'listing': listing
        }
        return render(request, "quizes/answer.html", context)