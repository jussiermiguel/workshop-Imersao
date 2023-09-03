from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer
# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet):
    """
    Esta ViewSet fornece operações padrão de CRUD para Aluno
    """
    queryset = Aluno.objects.all()# Pega todos os registros de Alunos
    serializer_class = AlunoSerializer # Usa AlunoSerializer para serializar os dados