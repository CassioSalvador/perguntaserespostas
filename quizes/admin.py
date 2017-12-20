from django.contrib import admin

# Importing the User and Group default apps
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

# Importing the AdminSite class to create a custom Admin page
from django.contrib.admin import AdminSite

from .models import Quiz, FatherQuiz

# Creating a custom AdminSite
class MyAdminSite(AdminSite):
    site_header = 'Perguntas e Respostas administration'

# Instanciating a new AdminSite
admin_site = MyAdminSite(name='myadmin')

# Register your models here.

# Creating a customized way to show a child quiz inside the father quizes
class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 0

# Creating a customized way to show father quizes
class FatherQuizAdmin(admin.ModelAdmin):
    # Fields to be displayed during the listing
    list_display = ('id', 'title', 'username', 'url')
    # Filter applied to search for a specific user
    list_filter = ('username',)
    # Read-only fields
    readonly_fields = ('url', 'username')
    # Fields to be shown
    fieldsets = [
        ('Father Quiz', {'fields': ['title', 'username', 'url']}),
    ]
    # Showing children quizes
    inlines = [QuizInline]

# Registering the FatherQuiz model and the FatherQuizAdmin (admin model) so it can be properly rendered
admin_site.register(FatherQuiz, FatherQuizAdmin)

# Registering the User and Group default models
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)