"""per_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
#from django.contrib import admin
from quizes.admin import admin_site
from django.views.generic import TemplateView
from quizes.views import Register, Profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin_site.urls),
    url(r'^register/success/$', TemplateView.as_view(template_name="registration/success.html"), name='register-success'),
    url(r'^register/$', Register.as_view(), name='register'),
    #url(r'^profile/$', login_required(Profile.as_view()), name='profile'),
    url(r'^profile/$', Profile.as_view(), name='profile'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('quizes.urls')),
]
