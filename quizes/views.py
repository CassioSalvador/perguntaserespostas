from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import QuizForm

# Create your views here.
def index(request):
    return render(request, "quizes/index.html")

class QuizRegister(View):
    form_class = QuizForm
    initial = {'key': 'value'}
    
    def get(self, request, *args, **kwargs):
        submitted = False
        form = self.form_class(initial=self.initial)
        if 'submitted' in request.GET:
            submitted = True
        return render(request, "quizes/register.html", {'form': form, 'submitted': submitted})
    
    def post(self, request, *args, **kwargs):
        submitted = False
        form = self.form_class(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            quiz.url = "http://127.0.0.1:8000/quiz/" + str(quiz.id)
            quiz.save()
            return HttpResponseRedirect('/register?submitted=True')
        return render(request, "quizes/register.html", {'form': form, 'submitted': submitted})

class AnswerQuiz(View):
    form_class = QuizForm
