from django.conf.urls import url
from . import views
from .views import QuizRegister, AnswerQuiz, FatherQuizList


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'quiz_registration/$', QuizRegister.as_view(), name='quiz_registration'),
    url(r'^quiz/(?P<fquiz_id>[0-9]+)/$', AnswerQuiz.as_view(), name='answer'),
    url(r'^quiz_list/$', FatherQuizList.as_view(), name='quiz_list'),
]