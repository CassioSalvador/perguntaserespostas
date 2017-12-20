from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
#Imports for the user management
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import QuizForm, FatherQuizForm

# Create your views here.
def index(request):
    return render(request, "quizes/index.html")

#class QuizRegister(View):
#    form_class = QuizForm
#    initial = {'key': 'value'}
    
#    def get(self, request, *args, **kwargs):
#        submitted = False
#        form = self.form_class(initial=self.initial)
#        if 'submitted' in request.GET:
#            submitted = True
#        return render(request, "quizes/register.html", {'form': form, 'submitted': submitted})
    
#    def post(self, request, *args, **kwargs):
#        submitted = False
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            fatherQuiz = form.save(commit=False)
            #Creating the children quizes
#            for key, 
            #Saving the user related to the quiz
#            try:
#                fatherQuiz.username = request.user
#            except Exception:
#                pass
#            fatherQuiz.save()
           # quiz.url = "http://127.0.0.1:8000/quiz/" + str(quiz.id)
           # quiz.save()
#            return HttpResponseRedirect('/register?submitted=True')
#        return render(request, "quizes/register.html", {'form': form, 'submitted': submitted})

class QuizRegister(View):
    quizform_formclass = QuizForm
    quizforms = []
    fatherquizform_formclass = FatherQuizForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        submitted = False
        quizform = self.quizform_formclass(initial=self.initial)
        fatherquizform = self.fatherquizform_formclass(initial=self.initial)
        if 'submitted' in request.GET:
            submitted = True
        return render(request, "quizes/register.html", {'quizform': quizform, 'fatherquizform': fatherquizform, 'submitted': submitted})

    def post(self, request, *args, **kwargs):
        submitted = False
        quizform = self.quizform_formclass(request.POST)
        fatherquizform = self.fatherquizform_formclass(request.POST)
        if quizform.is_valid() & fatherquizform.is_valid():
            fatherQuiz = fatherquizform.save(commit=False)
            fatherQuiz.save()
            Quiz = quizform.save(commit=False)
            #Quiz.fatherquiz = fatherQuiz.id
            Quiz.save()
            fatherQuiz.url = "http://127.0.0.1:8000/quiz/" + str(fatherQuiz.id)
            fatherQuiz.save()
            return HttpResponseRedirect('/register?submitted=True')
        return render(request, "quizes/register.html", {'quizform': quizform, 'fatherquizform': fatherquizform, 'submitted': submitted})
            


class AnswerQuiz(View):
    form_class = QuizForm

#fatherQuiz = new FatherQuiz
#fatherQuiz.save()
#newQuizes = []

#for key, question in questions:
  #quiz = new Quiz
  #quiz.question = question
  #quiz.rightOption = rightOption[key]
  #quiz.firstOption = firstOption[key]
 # quiz.fatheQuiz_id = fatherQuiz.id
  #quiz.save();