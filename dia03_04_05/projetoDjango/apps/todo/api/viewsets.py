from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Task
from .serializers import TaskSerializer
# importante o ponto para procurar o serializers dentro da mesma pasta que esta o viewsets

class TaskViewSet(ModelViewSet):
    
    # quero todos os dados que estao na tabela Task
    queryset = Task.objects.all() # obrigatório > chamada para o banco de dados
    
    serializer_class = TaskSerializer # 