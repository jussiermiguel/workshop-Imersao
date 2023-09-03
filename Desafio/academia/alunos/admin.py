from django.contrib import admin
from .models import Aluno

# o Aluno para que ele seja gerenciável no Django Admin
admin.site.register(Aluno)