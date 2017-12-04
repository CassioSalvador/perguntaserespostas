from django.conf.urls import url
from . import views
from .views import QuizRegister


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/$', QuizRegister.as_view(), name='register')
]