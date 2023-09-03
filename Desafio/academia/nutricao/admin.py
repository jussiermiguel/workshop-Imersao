from django.contrib import admin
from .models import ConsultaNutricionista

# Permite que a ConsultaNutricionista seja gerenciável no Django Admin
admin.site.register(ConsultaNutricionista)