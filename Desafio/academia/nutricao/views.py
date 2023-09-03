
from rest_framework import viewsets
from .models import ConsultaNutricionista
from .serializers import NutricionistaSerializer
# Create your views here.
class NutricionistaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaNutricionista.objects.all()# Pega todos os registros de consultas nutricionais
    serializer_class = NutricionistaSerializer# Usa NutricionistaSerializer para formatar os dados