from django.conf.urls import url
from . import views
from .views import QuizRegister


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'quiz_registration/$', QuizRegister.as_view(), name='quiz_registration')
]